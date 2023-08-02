# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, Mapping, Union, TYPE_CHECKING, overload, Optional, Type
from typing_extensions import Protocol  # type: ignore

if TYPE_CHECKING:
    from .._message_protocol import MessageContent, MessageType, SchemaContentValidate
    from ...aio._schema_registry_client_async import SchemaRegistryClient


# TODO: update docstring params/kwargs
# TODO: does protobuf need separate validation method? no, the encoding
# checks that data is valid against schema
class SchemaEncoder(Protocol):
    def __init__(
        self,
        *,
        client: "SchemaRegistryClient",
        validate: "SchemaContentValidate",
    ) -> None:
        """
        Provides the ability to encode and decode content according to the given schema of type `format`.
        """

    @property
    def mime_type(self) -> str:
        """
         Returns the MIME type associated string schema format type, such as "appliation/json; serialization=Avro".
        """

    @overload
    async def encode(
        self,
        content: Mapping[str, Any],
        *,
        schema_id: str,
        message_type: None = None,
        request_options: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> "MessageContent":
        ...

    @overload
    async def encode(
        self,
        content: Mapping[str, Any],
        *,
        schema_id: str,
        message_type: Type["MessageType"],
        request_options: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> "MessageType":
        ...

    async def encode(
        self,
        content: Mapping[str, Any],
        *,
        schema_id: str,
        message_type: Optional[Type["MessageType"]] = None,
        request_options: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Union["MessageType", "MessageContent"]:
        """
        Returns either a TypedDict or MessageType object with the data encoded with the schema format and content-type.
         If `validate` callable was passed in, will validate content against schema before encoding.
        """

    async def decode(
        self,  # pylint: disable=unused-argument
        message: "MessageType",
        *,
        request_options: Dict[str, Any] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Returns the decoded data with the schema format specified by the `content-type` property.
         If `validate` callable was passed to constructor, will validate content against schema after decoding.
        """
