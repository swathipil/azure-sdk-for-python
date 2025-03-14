# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import


from ._models_py3 import (  # type: ignore
    AddRemoveIncrementalNamedPartitionScalingMechanism,
    AdditionalNetworkInterfaceConfiguration,
    ApplicationHealthPolicy,
    ApplicationResource,
    ApplicationResourceList,
    ApplicationTypeResource,
    ApplicationTypeResourceList,
    ApplicationTypeUpdateParameters,
    ApplicationTypeVersionResource,
    ApplicationTypeVersionResourceList,
    ApplicationTypeVersionUpdateParameters,
    ApplicationTypeVersionsCleanupPolicy,
    ApplicationUpdateParameters,
    ApplicationUpgradePolicy,
    ApplicationUserAssignedIdentity,
    AvailableOperationDisplay,
    AveragePartitionLoadScalingTrigger,
    AverageServiceLoadScalingTrigger,
    AzureActiveDirectory,
    ClientCertificate,
    ClusterHealthPolicy,
    ClusterMonitoringPolicy,
    ClusterUpgradeDeltaHealthPolicy,
    ClusterUpgradePolicy,
    EndpointRangeDescription,
    ErrorModel,
    ErrorModelError,
    FrontendConfiguration,
    IpConfiguration,
    IpConfigurationPublicIPAddressConfiguration,
    IpTag,
    LoadBalancingRule,
    LongRunningOperationResult,
    ManagedAzResiliencyStatus,
    ManagedCluster,
    ManagedClusterCodeVersionResult,
    ManagedClusterListResult,
    ManagedClusterUpdateParameters,
    ManagedIdentity,
    ManagedMaintenanceWindowStatus,
    ManagedProxyResource,
    ManagedVMSize,
    ManagedVMSizesResult,
    NamedPartitionScheme,
    NetworkSecurityRule,
    NodeType,
    NodeTypeActionParameters,
    NodeTypeAvailableSku,
    NodeTypeListResult,
    NodeTypeListSkuResult,
    NodeTypeNatConfig,
    NodeTypeSku,
    NodeTypeSkuCapacity,
    NodeTypeSupportedSku,
    NodeTypeUpdateParameters,
    OperationListResult,
    OperationResult,
    Partition,
    PartitionInstanceCountScaleMechanism,
    ProxyResource,
    Resource,
    ResourceAzStatus,
    RollingUpgradeMonitoringPolicy,
    RuntimeResumeApplicationUpgradeParameters,
    ScalingMechanism,
    ScalingPolicy,
    ScalingTrigger,
    ServiceCorrelation,
    ServiceEndpoint,
    ServiceLoadMetric,
    ServicePlacementInvalidDomainPolicy,
    ServicePlacementNonPartiallyPlaceServicePolicy,
    ServicePlacementPolicy,
    ServicePlacementPreferPrimaryDomainPolicy,
    ServicePlacementRequireDomainDistributionPolicy,
    ServicePlacementRequiredDomainPolicy,
    ServiceResource,
    ServiceResourceList,
    ServiceResourceProperties,
    ServiceResourcePropertiesBase,
    ServiceTypeHealthPolicy,
    ServiceUpdateParameters,
    SettingsParameterDescription,
    SettingsSectionDescription,
    SingletonPartitionScheme,
    Sku,
    StatefulServiceProperties,
    StatelessServiceProperties,
    SubResource,
    Subnet,
    SystemData,
    UniformInt64RangePartitionScheme,
    UserAssignedIdentity,
    VMSSExtension,
    VMSize,
    VaultCertificate,
    VaultSecretGroup,
    VmApplication,
    VmImagePlan,
    VmManagedIdentity,
    VmssDataDisk,
)

from ._service_fabric_managed_clusters_management_client_enums import (  # type: ignore
    Access,
    AutoGeneratedDomainNameLabelScope,
    ClusterState,
    ClusterUpgradeCadence,
    ClusterUpgradeMode,
    Direction,
    DiskType,
    EvictionPolicyType,
    FailureAction,
    IPAddressType,
    ManagedClusterAddOnFeature,
    ManagedClusterVersionEnvironment,
    ManagedIdentityType,
    ManagedResourceProvisioningState,
    MoveCost,
    NodeTypeSkuScaleType,
    NsgProtocol,
    OsType,
    PartitionScheme,
    PrivateEndpointNetworkPolicies,
    PrivateIPAddressVersion,
    PrivateLinkServiceNetworkPolicies,
    ProbeProtocol,
    Protocol,
    PublicIPAddressVersion,
    RollingUpgradeMode,
    SecurityType,
    ServiceCorrelationScheme,
    ServiceKind,
    ServiceLoadMetricWeight,
    ServicePackageActivationMode,
    ServicePlacementPolicyType,
    ServiceScalingMechanismKind,
    ServiceScalingTriggerKind,
    SkuName,
    UpdateType,
    UpgradeMode,
    VmSetupAction,
    VmssExtensionSetupOrder,
    ZonalUpdateMode,
)
from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AddRemoveIncrementalNamedPartitionScalingMechanism",
    "AdditionalNetworkInterfaceConfiguration",
    "ApplicationHealthPolicy",
    "ApplicationResource",
    "ApplicationResourceList",
    "ApplicationTypeResource",
    "ApplicationTypeResourceList",
    "ApplicationTypeUpdateParameters",
    "ApplicationTypeVersionResource",
    "ApplicationTypeVersionResourceList",
    "ApplicationTypeVersionUpdateParameters",
    "ApplicationTypeVersionsCleanupPolicy",
    "ApplicationUpdateParameters",
    "ApplicationUpgradePolicy",
    "ApplicationUserAssignedIdentity",
    "AvailableOperationDisplay",
    "AveragePartitionLoadScalingTrigger",
    "AverageServiceLoadScalingTrigger",
    "AzureActiveDirectory",
    "ClientCertificate",
    "ClusterHealthPolicy",
    "ClusterMonitoringPolicy",
    "ClusterUpgradeDeltaHealthPolicy",
    "ClusterUpgradePolicy",
    "EndpointRangeDescription",
    "ErrorModel",
    "ErrorModelError",
    "FrontendConfiguration",
    "IpConfiguration",
    "IpConfigurationPublicIPAddressConfiguration",
    "IpTag",
    "LoadBalancingRule",
    "LongRunningOperationResult",
    "ManagedAzResiliencyStatus",
    "ManagedCluster",
    "ManagedClusterCodeVersionResult",
    "ManagedClusterListResult",
    "ManagedClusterUpdateParameters",
    "ManagedIdentity",
    "ManagedMaintenanceWindowStatus",
    "ManagedProxyResource",
    "ManagedVMSize",
    "ManagedVMSizesResult",
    "NamedPartitionScheme",
    "NetworkSecurityRule",
    "NodeType",
    "NodeTypeActionParameters",
    "NodeTypeAvailableSku",
    "NodeTypeListResult",
    "NodeTypeListSkuResult",
    "NodeTypeNatConfig",
    "NodeTypeSku",
    "NodeTypeSkuCapacity",
    "NodeTypeSupportedSku",
    "NodeTypeUpdateParameters",
    "OperationListResult",
    "OperationResult",
    "Partition",
    "PartitionInstanceCountScaleMechanism",
    "ProxyResource",
    "Resource",
    "ResourceAzStatus",
    "RollingUpgradeMonitoringPolicy",
    "RuntimeResumeApplicationUpgradeParameters",
    "ScalingMechanism",
    "ScalingPolicy",
    "ScalingTrigger",
    "ServiceCorrelation",
    "ServiceEndpoint",
    "ServiceLoadMetric",
    "ServicePlacementInvalidDomainPolicy",
    "ServicePlacementNonPartiallyPlaceServicePolicy",
    "ServicePlacementPolicy",
    "ServicePlacementPreferPrimaryDomainPolicy",
    "ServicePlacementRequireDomainDistributionPolicy",
    "ServicePlacementRequiredDomainPolicy",
    "ServiceResource",
    "ServiceResourceList",
    "ServiceResourceProperties",
    "ServiceResourcePropertiesBase",
    "ServiceTypeHealthPolicy",
    "ServiceUpdateParameters",
    "SettingsParameterDescription",
    "SettingsSectionDescription",
    "SingletonPartitionScheme",
    "Sku",
    "StatefulServiceProperties",
    "StatelessServiceProperties",
    "SubResource",
    "Subnet",
    "SystemData",
    "UniformInt64RangePartitionScheme",
    "UserAssignedIdentity",
    "VMSSExtension",
    "VMSize",
    "VaultCertificate",
    "VaultSecretGroup",
    "VmApplication",
    "VmImagePlan",
    "VmManagedIdentity",
    "VmssDataDisk",
    "Access",
    "AutoGeneratedDomainNameLabelScope",
    "ClusterState",
    "ClusterUpgradeCadence",
    "ClusterUpgradeMode",
    "Direction",
    "DiskType",
    "EvictionPolicyType",
    "FailureAction",
    "IPAddressType",
    "ManagedClusterAddOnFeature",
    "ManagedClusterVersionEnvironment",
    "ManagedIdentityType",
    "ManagedResourceProvisioningState",
    "MoveCost",
    "NodeTypeSkuScaleType",
    "NsgProtocol",
    "OsType",
    "PartitionScheme",
    "PrivateEndpointNetworkPolicies",
    "PrivateIPAddressVersion",
    "PrivateLinkServiceNetworkPolicies",
    "ProbeProtocol",
    "Protocol",
    "PublicIPAddressVersion",
    "RollingUpgradeMode",
    "SecurityType",
    "ServiceCorrelationScheme",
    "ServiceKind",
    "ServiceLoadMetricWeight",
    "ServicePackageActivationMode",
    "ServicePlacementPolicyType",
    "ServiceScalingMechanismKind",
    "ServiceScalingTriggerKind",
    "SkuName",
    "UpdateType",
    "UpgradeMode",
    "VmSetupAction",
    "VmssExtensionSetupOrder",
    "ZonalUpdateMode",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
