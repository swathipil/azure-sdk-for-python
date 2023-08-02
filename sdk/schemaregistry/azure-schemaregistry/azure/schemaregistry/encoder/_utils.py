# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from typing import (
    Any,
    Callable,
    Optional,
    Type,
    Union,
    cast,
    TypeVar,
    Mapping
)
import json
from functools import lru_cache

try:
    import jsonschema
except ImportError:
    pass

from ._exceptions import (  # pylint: disable=import-error
    InvalidContentError,
)
from ._message_protocol import (  # pylint: disable=import-error
    MessageContent,
    MessageType as MessageTypeProtocol,
)
from ._constants import (  # pylint: disable=import-error
    JSON_MIME_TYPE,
)

MessageType = TypeVar("MessageType", bound=MessageTypeProtocol)

def jsonschema_validate(schema: Mapping[str, Any], content: Mapping[str, Any]) -> None:
    """
    Validates content against provided schema using `jsonschema.Draft4Validator`.
     If invalid, raises Exception. Else, returns None.
     If jsonschema is not installed, raises ValueError.
     :param mapping[str, any] schema: The schema to validate against.
     :param mapping[str, any] content: The content to validate.
    """
    jsonschema.Draft4Validator(schema).validate(content)

@lru_cache(maxsize=128)
def load_schema(schema_definition: str) -> Mapping[str, Any]:
    return json.loads(schema_definition)

def create_message_content(
    validate: Callable,
    content: Mapping[str, Any],
    schema_definition: str,
    schema_id: str,
    message_type: Optional[Type[MessageType]] = None,
    **kwargs: Any,
) -> Union[MessageType, MessageContent]:
    content_type = f"{JSON_MIME_TYPE}+{schema_id}"

    try:
        # validate content
        schema = load_schema(schema_definition)
        validate(schema, content)
    except NameError as exc:
        raise ValueError(
            "To use default validation, please install `jsonschema` " \
            "using `pip install azure-schemaregistry[jsonencoder]` or pass another callable to `validate`."
        ) from exc
    except Exception as exc:  # pylint:disable=broad-except
        raise InvalidContentError(
            f"Invalid content value '{content}' for the following schema with schema ID {schema_id}:"
            f"{schema_definition}",
            details={"schema_id": f"{schema_id}"},
    ) from exc

    try:
        content_bytes = json.dumps(content, separators=(',', ':')).encode()
    except Exception as exc:
        raise InvalidContentError(
            f"Cannot encode value '{content}' for the following schema with schema ID {schema_id}:"
            f"{json.dumps(schema_definition)}",
            details={"schema_id": f"{schema_id}"},
        ) from exc

    if message_type:
        try:
            return cast(
                MessageType,
                message_type.from_message_content(content_bytes, content_type, **kwargs),
            )
        except AttributeError as exc:
            raise TypeError(
                f"""Cannot set content and content type on model object. The content model
                    {str(message_type)} must be a subtype of the MessageType protocol.
                    If using an Azure SDK model class, please check the README.md for the full list
                    of supported Azure SDK models and their corresponding versions.""",
                {"content": content_bytes, "content_type": content_type},
            ) from exc

    return MessageContent({"content": content_bytes, "content_type": content_type})


def parse_message(
    message: Union[MessageType, MessageContent]
):
    try:
        message = cast(MessageType, message)
        message_content_dict = message.__message_content__()
        content = message_content_dict["content"]
        content_type = message_content_dict["content_type"]
    except AttributeError:
        message = cast(MessageContent, message)
        try:
            content = message["content"]
            content_type = message["content_type"]
        except (KeyError, TypeError) as exc:
            raise TypeError(
                f"""The content model {str(message)} must be a subtype of the MessageType protocol or type
                    MessageContent. If using an Azure SDK model class, please check the README.md
                    for the full list of supported Azure SDK models and their corresponding versions."""
            ) from exc

    try:
        content_type_parts = content_type.split("+")
        if len(content_type_parts) != 2 or content_type_parts[0] != JSON_MIME_TYPE:
            raise InvalidContentError(
                f"Content type {content_type} was not in the expected format of JSON MIME type + schema ID."
            )
        schema_id = content_type_parts[1]
    except AttributeError:
        raise InvalidContentError(
            f"Content type {content_type} was not in the expected format of JSON MIME type + schema ID."
        )

    return schema_id, content


def decode_content(
    content: bytes,
    schema_id: str,
    schema_definition: str,
    validate: Optional[Callable],
):
    try:
        content = json.loads(content)
    except Exception as exc:
        error_message = (
            f"Cannot decode value '{content!r}' for schema with schema ID {schema_id}: {schema_definition}"
        )
        raise InvalidContentError(
            error_message,
            details={
                "schema_id": f"{schema_id}",
                "schema_definition": f"{schema_definition}",
            },
        ) from exc

    try:
        schema = load_schema(schema_definition)
        validate(schema, content)
    except NameError:
        raise ValueError(
            "To use default validation, please install `jsonschema` " \
            "using `pip install azure-schemaregistry[json]` or pass another callable to `validate`."
        )
    except Exception as exc:
        error_message = (
            f"Invalid content value '{content!r}' for schema with schema ID {schema_id}: {schema_definition}"
        )
        raise InvalidContentError(
            error_message,
            details={
                "schema_id": f"{schema_id}",
                "schema_definition": f"{schema_definition}",
            },
        ) from exc

    return content
