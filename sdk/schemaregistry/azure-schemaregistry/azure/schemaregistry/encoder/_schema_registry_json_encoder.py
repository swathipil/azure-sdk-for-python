# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
from __future__ import annotations
import logging
from functools import lru_cache
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Mapping,
    Optional,
    Type,
    overload,
    Union,
)

from ._utils import (  # pylint: disable=import-error
    create_message_content,
    parse_message,
    decode_content,
    MessageType,
    jsonschema_validate
)
from ._constants import JSON_MIME_TYPE
from ._message_protocol import (  # pylint: disable=import-error
    MessageContent,
)

if TYPE_CHECKING:
    from azure.schemaregistry import SchemaRegistryClient
    from azure.schemaregistry.encoder import SchemaContentValidate

_LOGGER = logging.getLogger(__name__)


class JsonSchemaEncoder(object):
    """
    JsonSchemaEncoder provides the ability to encode, validate, and decode content according
     to the schema ID corresponding to a pre-registerd JSON schema. It will automatically get
     and cache the schema.

    :keyword client: Required. The schema registry client which is used to register schema
     and retrieve schema from the service.
    :paramtype client: ~azure.schemaregistry.SchemaRegistryClient
    :keyword validate: Required. Callable that validates the content against the pre-registered schema corresponding
     to the provided schema ID. Must validate against schema draft version supported by the Schema Registry service.
     To use `jsonschema.Draft4Validator`, the default validation, `jsonschema` MUST be installed and is included in
     `extras_require` under `jsonencoder`. If validation callable is provided, all errors will be wrapped and raised as
     an ~azure.schemaregistry.encoder.InvalidContentError.
    :paramtype validate: ~azure.schemaregistry.encoder.SchemaContentValidate
    """

    def __init__(
        self,
        *,
        client: "SchemaRegistryClient",
        validate: "SchemaContentValidate" = jsonschema_validate,
    ) -> None:
        self._schema_registry_client = client
        self._validate = validate

    def __enter__(self) -> "JsonSchemaEncoder":
        self._schema_registry_client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._schema_registry_client.__exit__(*exc_details)

    @property
    def mime_type(self) -> str:
        """
         Returns the JSON MIME type.
        """
        return JSON_MIME_TYPE

    def close(self) -> None:
        """This method is to close the sockets opened by the client.
        It need not be used when using with a context manager.
        """
        self._schema_registry_client.close()

    @lru_cache(maxsize=128)
    def _get_schema(self, schema_id: str, **kwargs: Any) -> str:
        """
        Get schema content from local cache with the given schema id.
        If there is no item in the local cache, get schema from the service and cache it.

        :param str schema_id: Schema id
        :return: Schema content
        :rtype: str
        """
        schema_str = self._schema_registry_client.get_schema(
            schema_id, **kwargs
        ).definition
        return schema_str

    @overload
    def encode(
        self,
        content: Mapping[str, Any],
        *,
        schema_id: str,
        message_type: Type[MessageType],
        request_options: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> MessageType:
        ...

    @overload
    def encode(
        self,
        content: Mapping[str, Any],
        *,
        schema_id: str,
        message_type: None = None,
        request_options: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> MessageContent:
        ...

    def encode(
        self,
        content: Mapping[str, Any],
        *,
        schema_id: str,
        message_type: Optional[Type[MessageType]] = None,
        request_options: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Union[MessageType, MessageContent]:
        """Encodes content after validating against the pre-registered schema corresponding to the provided schema ID.
         If provided with a MessageType subtype, encoded content and content type will be passed to create message
         object. If not provided, the following dict will be returned:
         {"content": JSON encoded value, "content_type": JSON mime type string + schema ID}.

        If `message_type` is set, then additional keyword arguments will be passed to the message callback
         function provided.

        :param content: The content to be encoded.
        :type content: Mapping[str, Any]
        :keyword schema_id: The schema ID corresponding to the pre-registered schema used to encode the content.
        :paramtype schema_id: str
        :keyword message_type: The message class to construct the message. Must be a subtype of the
         azure.schemaregistry.encoder.MessageType protocol.
        :paramtype message_type: Type[MessageType] or None
        :keyword request_options: The keyword arguments for http requests to be passed to the client.
        :paramtype request_options: Dict[str, Any]
        :rtype: MessageType or MessageContent
        :raises ~azure.schemaregistry.encoder.InvalidSchemaError:
            Indicates an issue with validating schema.
        :raises ~azure.schemaregistry.encoder.InvalidContentError:
            Indicates an issue with encoding content with schema.
        """
        cache_misses = (
            self._get_schema.cache_info().misses  # pylint: disable=no-value-for-parameter
        )
        request_options = request_options or {}
        schema_definition = self._get_schema(schema_id, **request_options)
        new_cache_misses = (
            self._get_schema.cache_info().misses  # pylint: disable=no-value-for-parameter
        )
        if new_cache_misses > cache_misses:
            cache_info = (
                self._get_schema.cache_info()  # pylint: disable=no-value-for-parameter
            )
            _LOGGER.info(
                "New entry has been added to schema cache. Cache info: %s",
                str(cache_info),
            )

        return create_message_content(
            content=content,
            schema_definition=schema_definition,
            schema_id=schema_id,
            message_type=message_type,
            validate=self._validate,
            **kwargs,
        )

    def decode(
        self,  # pylint: disable=unused-argument
        message: Union[MessageContent, MessageType],
        *,
        request_options: Dict[str, Any] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """Decode bytes content and validate using the callable provided in the constructor and the pre-registered
         schema corresponding to the schema ID in the content type field.

        :param message: The message object which holds the content to be decoded and content type
         containing the schema ID. 
        :type message: MessageType or MessageContent
        :keyword request_options: The keyword arguments for http requests to be passed to the client.
        :paramtype request_options: Dict[str, Any]
        :rtype: Dict[str, Any]
        :raises ~azure.schemaregistry.encoder.InvalidSchemaError:
            Indicates an issue with validating schemas.
        :raises ~azure.schemaregistry.encoder.InvalidContentError:
            Indicates an issue with decoding content.
        """
        schema_id, content = parse_message(message)
        cache_misses = (
            self._get_schema.cache_info().misses  # pylint: disable=no-value-for-parameter
        )
        request_options = request_options or {}
        schema_definition = self._get_schema(schema_id, **request_options)
        new_cache_misses = (
            self._get_schema.cache_info().misses  # pylint: disable=no-value-for-parameter
        )
        if new_cache_misses > cache_misses:
            cache_info = (
                self._get_schema.cache_info()  # pylint: disable=no-value-for-parameter
            )
            _LOGGER.info(
                "New entry has been added to schema cache. Cache info: %s",
                str(cache_info),
            )

        return decode_content(
            content=content,
            schema_id=schema_id,
            schema_definition=schema_definition,
            validate=self._validate,
            **kwargs
        )
