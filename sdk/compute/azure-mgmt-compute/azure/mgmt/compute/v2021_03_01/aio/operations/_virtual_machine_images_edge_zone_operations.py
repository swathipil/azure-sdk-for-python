# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, List, Optional, TypeVar

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._virtual_machine_images_edge_zone_operations import (
    build_get_request,
    build_list_offers_request,
    build_list_publishers_request,
    build_list_request,
    build_list_skus_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class VirtualMachineImagesEdgeZoneOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.compute.v2021_03_01.aio.ComputeManagementClient`'s
        :attr:`virtual_machine_images_edge_zone` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(
        self, location: str, edge_zone: str, publisher_name: str, offer: str, skus: str, version: str, **kwargs: Any
    ) -> _models.VirtualMachineImage:
        """Gets a virtual machine image in an edge zone.

        :param location: The name of a supported Azure region. Required.
        :type location: str
        :param edge_zone: The name of the edge zone. Required.
        :type edge_zone: str
        :param publisher_name: A valid image publisher. Required.
        :type publisher_name: str
        :param offer: A valid image publisher offer. Required.
        :type offer: str
        :param skus: A valid image SKU. Required.
        :type skus: str
        :param version: A valid image SKU version. Required.
        :type version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VirtualMachineImage or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2021_03_01.models.VirtualMachineImage
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2021-03-01"] = kwargs.pop("api_version", _params.pop("api-version", "2021-03-01"))
        cls: ClsType[_models.VirtualMachineImage] = kwargs.pop("cls", None)

        request = build_get_request(
            location=location,
            edge_zone=edge_zone,
            publisher_name=publisher_name,
            offer=offer,
            skus=skus,
            version=version,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudErrorAutoGenerated, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("VirtualMachineImage", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/edgeZones/{edgeZone}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus/{skus}/versions/{version}"
    }

    @distributed_trace_async
    async def list(
        self,
        location: str,
        edge_zone: str,
        publisher_name: str,
        offer: str,
        skus: str,
        expand: Optional[str] = None,
        top: Optional[int] = None,
        orderby: Optional[str] = None,
        **kwargs: Any
    ) -> List[_models.VirtualMachineImageResource]:
        """Gets a list of all virtual machine image versions for the specified location, edge zone,
        publisher, offer, and SKU.

        :param location: The name of a supported Azure region. Required.
        :type location: str
        :param edge_zone: The name of the edge zone. Required.
        :type edge_zone: str
        :param publisher_name: A valid image publisher. Required.
        :type publisher_name: str
        :param offer: A valid image publisher offer. Required.
        :type offer: str
        :param skus: A valid image SKU. Required.
        :type skus: str
        :param expand: The expand expression to apply on the operation. Default value is None.
        :type expand: str
        :param top: An integer value specifying the number of images to return that matches supplied
         values. Default value is None.
        :type top: int
        :param orderby: Specifies the order of the results returned. Formatted as an OData query.
         Default value is None.
        :type orderby: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of VirtualMachineImageResource or the result of cls(response)
        :rtype: list[~azure.mgmt.compute.v2021_03_01.models.VirtualMachineImageResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2021-03-01"] = kwargs.pop("api_version", _params.pop("api-version", "2021-03-01"))
        cls: ClsType[List[_models.VirtualMachineImageResource]] = kwargs.pop("cls", None)

        request = build_list_request(
            location=location,
            edge_zone=edge_zone,
            publisher_name=publisher_name,
            offer=offer,
            skus=skus,
            subscription_id=self._config.subscription_id,
            expand=expand,
            top=top,
            orderby=orderby,
            api_version=api_version,
            template_url=self.list.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudErrorAutoGenerated, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("[VirtualMachineImageResource]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/edgeZones/{edgeZone}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus/{skus}/versions"
    }

    @distributed_trace_async
    async def list_offers(
        self, location: str, edge_zone: str, publisher_name: str, **kwargs: Any
    ) -> List[_models.VirtualMachineImageResource]:
        """Gets a list of virtual machine image offers for the specified location, edge zone and
        publisher.

        :param location: The name of a supported Azure region. Required.
        :type location: str
        :param edge_zone: The name of the edge zone. Required.
        :type edge_zone: str
        :param publisher_name: A valid image publisher. Required.
        :type publisher_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of VirtualMachineImageResource or the result of cls(response)
        :rtype: list[~azure.mgmt.compute.v2021_03_01.models.VirtualMachineImageResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2021-03-01"] = kwargs.pop("api_version", _params.pop("api-version", "2021-03-01"))
        cls: ClsType[List[_models.VirtualMachineImageResource]] = kwargs.pop("cls", None)

        request = build_list_offers_request(
            location=location,
            edge_zone=edge_zone,
            publisher_name=publisher_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list_offers.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudErrorAutoGenerated, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("[VirtualMachineImageResource]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_offers.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/edgeZones/{edgeZone}/publishers/{publisherName}/artifacttypes/vmimage/offers"
    }

    @distributed_trace_async
    async def list_publishers(
        self, location: str, edge_zone: str, **kwargs: Any
    ) -> List[_models.VirtualMachineImageResource]:
        """Gets a list of virtual machine image publishers for the specified Azure location and edge zone.

        :param location: The name of a supported Azure region. Required.
        :type location: str
        :param edge_zone: The name of the edge zone. Required.
        :type edge_zone: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of VirtualMachineImageResource or the result of cls(response)
        :rtype: list[~azure.mgmt.compute.v2021_03_01.models.VirtualMachineImageResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2021-03-01"] = kwargs.pop("api_version", _params.pop("api-version", "2021-03-01"))
        cls: ClsType[List[_models.VirtualMachineImageResource]] = kwargs.pop("cls", None)

        request = build_list_publishers_request(
            location=location,
            edge_zone=edge_zone,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list_publishers.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudErrorAutoGenerated, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("[VirtualMachineImageResource]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_publishers.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/edgeZones/{edgeZone}/publishers"
    }

    @distributed_trace_async
    async def list_skus(
        self, location: str, edge_zone: str, publisher_name: str, offer: str, **kwargs: Any
    ) -> List[_models.VirtualMachineImageResource]:
        """Gets a list of virtual machine image SKUs for the specified location, edge zone, publisher, and
        offer.

        :param location: The name of a supported Azure region. Required.
        :type location: str
        :param edge_zone: The name of the edge zone. Required.
        :type edge_zone: str
        :param publisher_name: A valid image publisher. Required.
        :type publisher_name: str
        :param offer: A valid image publisher offer. Required.
        :type offer: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of VirtualMachineImageResource or the result of cls(response)
        :rtype: list[~azure.mgmt.compute.v2021_03_01.models.VirtualMachineImageResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2021-03-01"] = kwargs.pop("api_version", _params.pop("api-version", "2021-03-01"))
        cls: ClsType[List[_models.VirtualMachineImageResource]] = kwargs.pop("cls", None)

        request = build_list_skus_request(
            location=location,
            edge_zone=edge_zone,
            publisher_name=publisher_name,
            offer=offer,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list_skus.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudErrorAutoGenerated, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("[VirtualMachineImageResource]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_skus.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/edgeZones/{edgeZone}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus"
    }