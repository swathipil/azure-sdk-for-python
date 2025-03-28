# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._cloud_hsm_clusters_operations import CloudHsmClustersOperations
from ._cloud_hsm_cluster_private_link_resources_operations import CloudHsmClusterPrivateLinkResourcesOperations
from ._cloud_hsm_cluster_private_endpoint_connections_operations import (
    CloudHsmClusterPrivateEndpointConnectionsOperations,
)
from ._private_endpoint_connections_operations import PrivateEndpointConnectionsOperations
from ._cloud_hsm_cluster_backup_status_operations import CloudHsmClusterBackupStatusOperations
from ._cloud_hsm_cluster_restore_status_operations import CloudHsmClusterRestoreStatusOperations
from ._dedicated_hsm_operations import DedicatedHsmOperations
from ._operations import Operations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "CloudHsmClustersOperations",
    "CloudHsmClusterPrivateLinkResourcesOperations",
    "CloudHsmClusterPrivateEndpointConnectionsOperations",
    "PrivateEndpointConnectionsOperations",
    "CloudHsmClusterBackupStatusOperations",
    "CloudHsmClusterRestoreStatusOperations",
    "DedicatedHsmOperations",
    "Operations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
