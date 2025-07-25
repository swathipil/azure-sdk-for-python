# Release History

## 10.5.0b1 (2025-07-20)

### Features Added

  - Client `EventGridManagementClient` added operation group `partner_destinations`
  - Client `EventGridManagementClient` added operation group `network_security_perimeter_configurations`
  - Model `Channel` added property `partner_destination_info`
  - Enum `ChannelProvisioningState` added member `IDLE_DUE_TO_MIRRORED_PARTNER_DESTINATION_DELETION`
  - Enum `ChannelType` added member `PARTNER_DESTINATION`
  - Model `ChannelUpdateParameters` added property `partner_destination_info`
  - Model `Domain` added property `sku`
  - Model `DomainUpdateParameters` added property `sku`
  - Enum `EndpointType` added member `PARTNER_DESTINATION`
  - Model `EventSubscriptionIdentity` added property `federated_identity_credential_info`
  - Enum `PublicNetworkAccess` added member `SECURED_BY_PERIMETER`
  - Model `Subscription` added property `tags`
  - Model `SubscriptionUpdateParameters` added property `tags`
  - Model `Topic` added property `sku`
  - Model `Topic` added property `kind`
  - Model `Topic` added property `extended_location`
  - Model `TopicSpacesConfiguration` added property `client_authentication`
  - Model `TopicUpdateParameters` added property `sku`
  - Model `UpdateTopicSpacesConfigurationInfo` added property `client_authentication`
  - Model `VerifiedPartner` added property `partner_destination_details`
  - Added enum `AlternativeAuthenticationNameSource`
  - Added model `AzureADPartnerClientAuthentication`
  - Added model `ClientAuthenticationSettings`
  - Added model `CustomJwtAuthenticationManagedIdentity`
  - Added enum `CustomJwtAuthenticationManagedIdentityType`
  - Added model `CustomJwtAuthenticationSettings`
  - Added model `CustomWebhookAuthenticationManagedIdentity`
  - Added enum `CustomWebhookAuthenticationManagedIdentityType`
  - Added model `EncodedIssuerCertificateInfo`
  - Added model `ExtendedLocation`
  - Added model `FederatedIdentityCredentialInfo`
  - Added model `IssuerCertificateInfo`
  - Added enum `NetworkSecurityPerimeterAssociationAccessMode`
  - Added enum `NetworkSecurityPerimeterConfigProvisioningState`
  - Added model `NetworkSecurityPerimeterConfiguration`
  - Added enum `NetworkSecurityPerimeterConfigurationIssueSeverity`
  - Added enum `NetworkSecurityPerimeterConfigurationIssueType`
  - Added model `NetworkSecurityPerimeterConfigurationIssues`
  - Added model `NetworkSecurityPerimeterConfigurationList`
  - Added model `NetworkSecurityPerimeterConfigurationProfile`
  - Added model `NetworkSecurityPerimeterInfo`
  - Added model `NetworkSecurityPerimeterProfileAccessRule`
  - Added enum `NetworkSecurityPerimeterProfileAccessRuleDirection`
  - Added enum `NetworkSecurityPerimeterResourceType`
  - Added model `NetworkSecurityPerimeterSubscription`
  - Added model `PartnerClientAuthentication`
  - Added enum `PartnerClientAuthenticationType`
  - Added model `PartnerDestination`
  - Added enum `PartnerDestinationActivationState`
  - Added model `PartnerDestinationInfo`
  - Added enum `PartnerDestinationProvisioningState`
  - Added model `PartnerDestinationUpdateParameters`
  - Added model `PartnerDestinationsListResult`
  - Added enum `PartnerEndpointType`
  - Added model `PartnerEventSubscriptionDestination`
  - Added model `PartnerUpdateDestinationInfo`
  - Added model `ResourceAssociation`
  - Added enum `ResourceKind`
  - Added model `ResourceMoveChangeHistory`
  - Added model `ResourceSku`
  - Added enum `Sku`
  - Added model `WebhookAuthenticationSettings`
  - Added model `WebhookPartnerDestinationInfo`
  - Added model `WebhookUpdatePartnerDestinationInfo`
  - Added operation group `NetworkSecurityPerimeterConfigurationsOperations`
  - Added operation group `PartnerDestinationsOperations`

## 10.4.0 (2025-03-24)

### Features Added

  - Client `EventGridManagementClient` added operation group `ca_certificates`
  - Client `EventGridManagementClient` added operation group `client_groups`
  - Client `EventGridManagementClient` added operation group `clients`
  - Client `EventGridManagementClient` added operation group `namespace_topic_event_subscriptions`
  - Client `EventGridManagementClient` added operation group `namespaces`
  - Client `EventGridManagementClient` added operation group `namespace_topics`
  - Client `EventGridManagementClient` added operation group `permission_bindings`
  - Client `EventGridManagementClient` added operation group `topic_spaces`
  - Model `Domain` added property `minimum_tls_version_allowed`
  - Model `Domain` added property `event_type_info`
  - Model `DomainUpdateParameters` added property `minimum_tls_version_allowed`
  - Model `DomainUpdateParameters` added property `event_type_info`
  - Enum `EndpointType` added member `MONITOR_ALERT`
  - Enum `EndpointType` added member `NAMESPACE_TOPIC`
  - Model `PartnerNamespace` added property `minimum_tls_version_allowed`
  - Model `PartnerNamespaceUpdateParameters` added property `minimum_tls_version_allowed`
  - Enum `PrivateEndpointConnectionsParentType` added member `NAMESPACES`
  - Model `Topic` added property `event_type_info`
  - Model `Topic` added property `minimum_tls_version_allowed`
  - Model `TopicTypeInfo` added property `are_regional_and_global_sources_supported`
  - Model `TopicTypeInfo` added property `additional_enforced_permissions`
  - Model `TopicUpdateParameters` added property `minimum_tls_version_allowed`
  - Model `TopicUpdateParameters` added property `event_type_info`
  - Model `WebHookEventSubscriptionDestination` added property `minimum_tls_version_allowed`
  - Added model `BoolEqualsFilter`
  - Added model `CaCertificate`
  - Added enum `CaCertificateProvisioningState`
  - Added model `CaCertificatesListResult`
  - Added client `Client`
  - Added model `ClientCertificateAuthentication`
  - Added enum `ClientCertificateValidationScheme`
  - Added model `ClientGroup`
  - Added enum `ClientGroupProvisioningState`
  - Added model `ClientGroupsListResult`
  - Added enum `ClientProvisioningState`
  - Added enum `ClientState`
  - Added model `ClientsListResult`
  - Added model `CustomDomainConfiguration`
  - Added model `CustomDomainIdentity`
  - Added enum `CustomDomainIdentityType`
  - Added model `CustomDomainOwnershipValidationResult`
  - Added enum `CustomDomainValidationState`
  - Added model `DeliveryConfiguration`
  - Added enum `DeliveryMode`
  - Added enum `DeliverySchema`
  - Added model `DynamicRoutingEnrichment`
  - Added model `ErrorAdditionalInfo`
  - Added model `ErrorDetail`
  - Added model `ErrorResponse`
  - Added enum `EventInputSchema`
  - Added model `Filter`
  - Added enum `FilterOperatorType`
  - Added model `FiltersConfiguration`
  - Added model `IsNotNullFilter`
  - Added model `IsNullOrUndefinedFilter`
  - Added model `MonitorAlertEventSubscriptionDestination`
  - Added enum `MonitorAlertSeverity`
  - Added model `Namespace`
  - Added enum `NamespaceProvisioningState`
  - Added model `NamespaceRegenerateKeyRequest`
  - Added model `NamespaceSharedAccessKeys`
  - Added model `NamespaceSku`
  - Added model `NamespaceTopic`
  - Added model `NamespaceTopicEventSubscriptionDestination`
  - Added enum `NamespaceTopicProvisioningState`
  - Added model `NamespaceTopicUpdateParameters`
  - Added model `NamespaceTopicsListResult`
  - Added model `NamespaceUpdateParameters`
  - Added model `NamespacesListResult`
  - Added model `NumberGreaterThanFilter`
  - Added model `NumberGreaterThanOrEqualsFilter`
  - Added model `NumberInFilter`
  - Added model `NumberInRangeFilter`
  - Added model `NumberLessThanFilter`
  - Added model `NumberLessThanOrEqualsFilter`
  - Added model `NumberNotInFilter`
  - Added model `NumberNotInRangeFilter`
  - Added model `PermissionBinding`
  - Added enum `PermissionBindingProvisioningState`
  - Added model `PermissionBindingsListResult`
  - Added enum `PermissionType`
  - Added enum `PublisherType`
  - Added model `PushInfo`
  - Added model `QueueInfo`
  - Added model `RoutingEnrichments`
  - Added model `RoutingIdentityInfo`
  - Added enum `RoutingIdentityType`
  - Added enum `SkuName`
  - Added model `StaticRoutingEnrichment`
  - Added enum `StaticRoutingEnrichmentType`
  - Added model `StaticStringRoutingEnrichment`
  - Added model `StringBeginsWithFilter`
  - Added model `StringContainsFilter`
  - Added model `StringEndsWithFilter`
  - Added model `StringInFilter`
  - Added model `StringNotBeginsWithFilter`
  - Added model `StringNotContainsFilter`
  - Added model `StringNotEndsWithFilter`
  - Added model `StringNotInFilter`
  - Added model `Subscription`
  - Added model `SubscriptionFullUrl`
  - Added enum `SubscriptionProvisioningState`
  - Added model `SubscriptionUpdateParameters`
  - Added model `SubscriptionsListResult`
  - Added enum `TlsVersion`
  - Added model `TopicSpace`
  - Added enum `TopicSpaceProvisioningState`
  - Added model `TopicSpacesConfiguration`
  - Added enum `TopicSpacesConfigurationState`
  - Added model `TopicSpacesListResult`
  - Added model `TopicTypeAdditionalEnforcedPermission`
  - Added model `TopicsConfiguration`
  - Added model `UpdateTopicSpacesConfigurationInfo`
  - Added model `UpdateTopicsConfigurationInfo`
  - Added operation group `CaCertificatesOperations`
  - Added operation group `ClientGroupsOperations`
  - Added operation group `ClientsOperations`
  - Added operation group `NamespaceTopicEventSubscriptionsOperations`
  - Added operation group `NamespaceTopicsOperations`
  - Added operation group `NamespacesOperations`
  - Added operation group `PermissionBindingsOperations`
  - Added operation group `TopicSpacesOperations`

## 10.3.0b4 (2024-04-29)

### Features Added

  - Added operation NamespaceTopicEventSubscriptionsOperations.get_full_url
  - Added operation NamespacesOperations.begin_validate_custom_domain_ownership
  - Model ClientAuthenticationSettings has a new parameter custom_jwt_authentication
  - Model NamespaceUpdateParameters has a new parameter topics_configuration
  - Model PushInfo has a new parameter destination
  - Model Subscription has a new parameter expiration_time_utc
  - Model SubscriptionUpdateParameters has a new parameter expiration_time_utc
  - Model TopicSpacesConfiguration has a new parameter custom_domains
  - Model TopicsConfiguration has a new parameter custom_domains
  - Model UpdateTopicSpacesConfigurationInfo has a new parameter custom_domains

## 10.3.0b3 (2023-12-04)

### Features Added

  - Added operation NamespaceTopicEventSubscriptionsOperations.get_delivery_attributes
  - Added operation group NetworkSecurityPerimeterConfigurationsOperations
  - Model DeliveryConfiguration has a new parameter push
  - Model TopicTypeInfo has a new parameter additional_enforced_permissions

### Breaking Changes

  - Model Client no longer has parameter authentication
  - Parameter value_type of model StaticRoutingEnrichment is now required

## 10.3.0b2 (2023-05-19)

### Features Added

  - Added operation group CaCertificatesOperations
  - Added operation group ClientGroupsOperations
  - Added operation group ClientsOperations
  - Added operation group NamespaceTopicEventSubscriptionsOperations
  - Added operation group NamespaceTopicsOperations
  - Added operation group NamespacesOperations
  - Added operation group PartnerDestinationsOperations
  - Added operation group PermissionBindingsOperations
  - Added operation group TopicSpacesOperations
  - Model Channel has a new parameter partner_destination_info
  - Model ChannelUpdateParameters has a new parameter partner_destination_info
  - Model Domain has a new parameter event_type_info
  - Model Domain has a new parameter minimum_tls_version_allowed
  - Model Domain has a new parameter sku
  - Model DomainUpdateParameters has a new parameter event_type_info
  - Model DomainUpdateParameters has a new parameter minimum_tls_version_allowed
  - Model DomainUpdateParameters has a new parameter sku
  - Model PartnerNamespace has a new parameter minimum_tls_version_allowed
  - Model PartnerNamespaceUpdateParameters has a new parameter minimum_tls_version_allowed
  - Model Topic has a new parameter event_type_info
  - Model Topic has a new parameter extended_location
  - Model Topic has a new parameter kind
  - Model Topic has a new parameter minimum_tls_version_allowed
  - Model Topic has a new parameter sku
  - Model TopicTypeInfo has a new parameter are_regional_and_global_sources_supported
  - Model TopicUpdateParameters has a new parameter event_type_info
  - Model TopicUpdateParameters has a new parameter minimum_tls_version_allowed
  - Model TopicUpdateParameters has a new parameter sku
  - Model VerifiedPartner has a new parameter partner_destination_details
  - Model WebHookEventSubscriptionDestination has a new parameter minimum_tls_version_allowed

## 10.3.0b1 (2022-11-30)

### Other Changes

  - Added generated samples in github repo
  - Drop support for python<3.7.0

## 10.2.0 (2022-06-20)

**Features**

  - Added operation group ChannelsOperations
  - Added operation group DomainEventSubscriptionsOperations
  - Added operation group DomainTopicEventSubscriptionsOperations
  - Added operation group PartnerConfigurationsOperations
  - Added operation group PartnerNamespacesOperations
  - Added operation group PartnerRegistrationsOperations
  - Added operation group PartnerTopicEventSubscriptionsOperations
  - Added operation group PartnerTopicsOperations
  - Added operation group TopicEventSubscriptionsOperations
  - Added operation group VerifiedPartnersOperations
  - Model Domain has a new parameter data_residency_boundary
  - Model DomainUpdateParameters has a new parameter data_residency_boundary
  - Model Operation has a new parameter is_data_action
  - Model Topic has a new parameter data_residency_boundary
  - Model TopicUpdateParameters has a new parameter data_residency_boundary

## 10.2.0b2 (2022-05-30)

**Breaking changes**

  - Operation DomainEventSubscriptionsOperations.list has a new parameter filter
  - Operation DomainEventSubscriptionsOperations.list has a new parameter top
  - Operation DomainTopicEventSubscriptionsOperations.list has a new parameter filter
  - Operation DomainTopicEventSubscriptionsOperations.list has a new parameter top
  - Operation TopicEventSubscriptionsOperations.list has a new parameter filter
  - Operation TopicEventSubscriptionsOperations.list has a new parameter top

## 10.2.0b1 (2022-04-07)

**Features**

  - Added operation group ChannelsOperations
  - Added operation group DomainEventSubscriptionsOperations
  - Added operation group DomainTopicEventSubscriptionsOperations
  - Added operation group EventChannelsOperations
  - Added operation group PartnerConfigurationsOperations
  - Added operation group PartnerDestinationsOperations
  - Added operation group PartnerNamespacesOperations
  - Added operation group PartnerRegistrationsOperations
  - Added operation group PartnerTopicEventSubscriptionsOperations
  - Added operation group PartnerTopicsOperations
  - Added operation group TopicEventSubscriptionsOperations
  - Added operation group VerifiedPartnersOperations
  - Model Domain has a new parameter data_residency_boundary
  - Model Domain has a new parameter sku
  - Model DomainUpdateParameters has a new parameter data_residency_boundary
  - Model DomainUpdateParameters has a new parameter sku
  - Model Operation has a new parameter is_data_action
  - Model Topic has a new parameter data_residency_boundary
  - Model Topic has a new parameter extended_location
  - Model Topic has a new parameter kind
  - Model Topic has a new parameter sku
  - Model TopicUpdateParameters has a new parameter data_residency_boundary
  - Model TopicUpdateParameters has a new parameter sku

## 10.1.0 (2021-12-13)

**Features**

  - Added model NumberInRangeAdvancedFilter
  - Added model StringNotContainsAdvancedFilter
  - Added model NumberNotInRangeAdvancedFilter
  - Added model IsNullOrUndefinedAdvancedFilter
  - Added model IsNotNullAdvancedFilter
  - Added model StringNotBeginsWithAdvancedFilter
  - Added model StringNotEndsWithAdvancedFilter

## 10.0.0 (2021-10-21)

**Features**

  - Model Domain has a new parameter disable_local_auth
  - Model Domain has a new parameter auto_delete_topic_with_last_subscription
  - Model Domain has a new parameter auto_create_topic_with_first_subscription
  - Model Topic has a new parameter disable_local_auth
  - Model DomainUpdateParameters has a new parameter disable_local_auth
  - Model DomainUpdateParameters has a new parameter auto_delete_topic_with_last_subscription
  - Model DomainUpdateParameters has a new parameter auto_create_topic_with_first_subscription
  - Model ExtensionTopic has a new parameter system_data
  - Model TopicUpdateParameters has a new parameter disable_local_auth

**Breaking changes**

  - Model Domain no longer has parameter sku
  - Model Topic no longer has parameter sku
  - Model Topic no longer has parameter extended_location
  - Model Topic no longer has parameter kind
  - Model DomainUpdateParameters no longer has parameter sku
  - Model TopicUpdateParameters no longer has parameter sku
  - Removed operation group EventChannelsOperations
  - Removed operation group PartnerRegistrationsOperations
  - Removed operation group PartnerTopicEventSubscriptionsOperations
  - Removed operation group PartnerNamespacesOperations
  - Removed operation group PartnerTopicsOperations

## 9.0.0 (2021-05-24)

**Features**

  - Model EventHubEventSubscriptionDestination has a new parameter delivery_attribute_mappings
  - Model StorageQueueEventSubscriptionDestination has a new parameter queue_message_time_to_live_in_seconds
  - Model TopicTypeInfo has a new parameter supported_scopes_for_source
  - Model Topic has a new parameter extended_location
  - Model Topic has a new parameter kind
  - Model Topic has a new parameter system_data
  - Model Topic has a new parameter identity
  - Model Topic has a new parameter sku
  - Model EventSubscriptionFilter has a new parameter enable_advanced_filtering_on_arrays
  - Model AzureFunctionEventSubscriptionDestination has a new parameter delivery_attribute_mappings
  - Model EventSubscriptionUpdateParameters has a new parameter dead_letter_with_resource_identity
  - Model EventSubscriptionUpdateParameters has a new parameter delivery_with_resource_identity
  - Model ServiceBusQueueEventSubscriptionDestination has a new parameter delivery_attribute_mappings
  - Model DomainTopic has a new parameter system_data
  - Model DomainUpdateParameters has a new parameter sku
  - Model DomainUpdateParameters has a new parameter identity
  - Model HybridConnectionEventSubscriptionDestination has a new parameter delivery_attribute_mappings
  - Model TopicUpdateParameters has a new parameter sku
  - Model TopicUpdateParameters has a new parameter identity
  - Model ServiceBusTopicEventSubscriptionDestination has a new parameter delivery_attribute_mappings
  - Model Domain has a new parameter sku
  - Model Domain has a new parameter system_data
  - Model Domain has a new parameter identity
  - Model EventSubscription has a new parameter dead_letter_with_resource_identity
  - Model EventSubscription has a new parameter system_data
  - Model EventSubscription has a new parameter delivery_with_resource_identity
  - Model WebHookEventSubscriptionDestination has a new parameter delivery_attribute_mappings
  - Added operation TopicsOperations.begin_regenerate_key
  - Added operation EventSubscriptionsOperations.get_delivery_attributes
  - Added operation group PartnerRegistrationsOperations
  - Added operation group SystemTopicsOperations
  - Added operation group EventChannelsOperations
  - Added operation group PartnerNamespacesOperations
  - Added operation group ExtensionTopicsOperations
  - Added operation group PartnerTopicsOperations
  - Added operation group PartnerTopicEventSubscriptionsOperations
  - Added operation group SystemTopicEventSubscriptionsOperations

**Breaking changes**

  - Removed operation TopicsOperations.regenerate_key

## 8.0.0 (2020-12-21)

**Breaking changes**

  - Operation TopicsOperations.regenerate_key has a new signature
  - Operation DomainsOperations.regenerate_key has a new signature

## 8.0.0b1 (2020-10-31)

This is beta preview version.
For detailed changelog please refer to equivalent stable version 3.0.0rc8(https://pypi.org/project/azure-mgmt-eventgrid/3.0.0rc8/)

This version uses a next-generation code generator that introduces important breaking changes, but also important new features (like unified authentication and async programming).

**General breaking changes**

- Credential system has been completly revamped:

  - `azure.common.credentials` or `msrestazure.azure_active_directory` instances are no longer supported, use the `azure-identity` classes instead: https://pypi.org/project/azure-identity/
  - `credentials` parameter has been renamed `credential`

- The `config` attribute no longer exists on a client, configuration should be passed as kwarg. Example: `MyClient(credential, subscription_id, enable_logging=True)`. For a complete set of
  supported options, see the [parameters accept in init documentation of azure-core](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#available-policies)
- You can't import a `version` module anymore, use `__version__` instead
- Operations that used to return a `msrest.polling.LROPoller` now returns a `azure.core.polling.LROPoller` and are prefixed with `begin_`.
- Exceptions tree have been simplified and most exceptions are now `azure.core.exceptions.HttpResponseError` (`CloudError` has been removed).
- Most of the operation kwarg have changed. Some of the most noticeable:

  - `raw` has been removed. Equivalent feature can be found using `cls`, a callback that will give access to internal HTTP response for advanced user
  - For a complete set of supported options, see the [parameters accept in Request documentation of azure-core](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#available-policies)

**General new features**

- Type annotations support using `typing`. SDKs are mypy ready.
- This client has now stable and official support for async. Check the `aio` namespace of your package to find the async client.
- This client now support natively tracing library like OpenCensus or OpenTelemetry. See this [tracing quickstart](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/core/azure-core-tracing-opentelemetry) for an overview.

## 3.0.0rc8 (2020-06-05)

**Breaking changes**

  - Model EventSubscriptionUpdateParameters no longer has parameter dead_letter_with_resource_identity
  - Model EventSubscriptionUpdateParameters no longer has parameter delivery_with_resource_identity
  - Model DomainUpdateParameters no longer has parameter sku
  - Model DomainUpdateParameters no longer has parameter identity
  - Model Domain no longer has parameter sku
  - Model Domain no longer has parameter identity
  - Model EventSubscription no longer has parameter dead_letter_with_resource_identity
  - Model EventSubscription no longer has parameter delivery_with_resource_identity
  - Model TopicUpdateParameters no longer has parameter sku
  - Model TopicUpdateParameters no longer has parameter identity
  - Model Topic no longer has parameter sku
  - Model Topic no longer has parameter identity
  - Removed operation group ExtensionTopicsOperations
  - Removed operation group PartnerNamespacesOperations
  - Removed operation group PartnerRegistrationsOperations
  - Removed operation group PartnerTopicsOperations
  - Removed operation group SystemTopicEventSubscriptionsOperations
  - Removed operation group SystemTopicsOperations
  - Removed operation group PartnerTopicEventSubscriptionsOperations
  - Removed operation group EventChannelsOperations

## 3.0.0rc7 (2020-05-14)

**Features**

  - Model PartnerTopic has a new parameter expiration_time_if_not_activated_utc
  - Model PartnerTopic has a new parameter partner_topic_friendly_description
  - Model EventChannel has a new parameter partner_topic_readiness_state
  - Model EventChannel has a new parameter expiration_time_if_not_activated_utc
  - Model EventChannel has a new parameter partner_topic_friendly_description
  - Model PartnerRegistration has a new parameter partner_customer_service_number
  - Model PartnerRegistration has a new parameter partner_customer_service_extension
  - Model PartnerRegistration has a new parameter long_description
  - Model PartnerRegistration has a new parameter customer_service_uri

**Breaking changes**

  - Model EventChannelFilter has a new signature

## 3.0.0rc6 (2020-04-03)

**Features**

  - Model PartnerRegistrationUpdateParameters has a new parameter tags
  - Model EventChannel has a new parameter filter

**Breaking changes**

  - Operation PrivateEndpointConnectionsOperations.update has a new signature
  - Operation SystemTopicEventSubscriptionsOperations.list_by_system_topic has a new signature
  - Operation PartnerTopicEventSubscriptionsOperations.list_by_partner_topic has a new signature

## 3.0.0rc5 (2020-03-19)

**Features**

- Model Domain has a new parameter public_network_access
- Model Domain has a new parameter identity
- Model Domain has a new parameter private_endpoint_connections
- Model Domain has a new parameter sku
- Model DomainUpdateParameters has a new parameter public_network_access
- Model DomainUpdateParameters has a new parameter identity
- Model DomainUpdateParameters has a new parameter sku
- Model TopicUpdateParameters has a new parameter public_network_access
- Model TopicUpdateParameters has a new parameter identity
- Model TopicUpdateParameters has a new parameter sku
- Model EventSubscriptionUpdateParameters has a new parameter dead_letter_with_resource_identity
- Model EventSubscriptionUpdateParameters has a new parameter delivery_with_resource_identity
- Model Topic has a new parameter public_network_access
- Model Topic has a new parameter identity
- Model Topic has a new parameter private_endpoint_connections
- Model Topic has a new parameter sku
- Model EventSubscription has a new parameter dead_letter_with_resource_identity
- Model EventSubscription has a new parameter delivery_with_resource_identity
- Added operation group PrivateLinkResourcesOperations
- Added operation group SystemTopicsOperations
- Added operation group PrivateEndpointConnectionsOperations
- Added operation group PartnerTopicsOperations
- Added operation group PartnerNamespacesOperations
- Added operation group PartnerTopicEventSubscriptionsOperations
- Added operation group PartnerRegistrationsOperations
- Added operation group ExtensionTopicsOperations
- Added operation group SystemTopicEventSubscriptionsOperations
- Added operation group EventChannelsOperations

**Breaking changes**

- Model Domain no longer has parameter allow_traffic_from_all_ips
- Model DomainUpdateParameters no longer has parameter allow_traffic_from_all_ips
- Model TopicUpdateParameters no longer has parameter allow_traffic_from_all_ips
- Model Topic no longer has parameter allow_traffic_from_all_ips

## 3.0.0rc4 (2020-01-17)

**Features**

  - Model DomainUpdateParameters has a new parameter
    allow_traffic_from_all_ips
  - Model DomainUpdateParameters has a new parameter inbound_ip_rules
  - Model TopicUpdateParameters has a new parameter
    allow_traffic_from_all_ips
  - Model TopicUpdateParameters has a new parameter inbound_ip_rules

**Breaking changes**

  - Operation DomainsOperations.update has a new signature
  - Operation TopicsOperations.update has a new signature

## 3.0.0rc3 (2020-01-12)

**Features**

  - Model Domain has a new parameter allow_traffic_from_all_ips
  - Model Domain has a new parameter inbound_ip_rules
  - Model Topic has a new parameter allow_traffic_from_all_ips
  - Model Topic has a new parameter inbound_ip_rules
  - Model TopicTypeInfo has a new parameter source_resource_format

## 3.0.0rc2 (2019-11-11)

**Features**

  - Model WebHookEventSubscriptionDestination has a new parameter
    azure_active_directory_tenant_id

## 3.0.0rc1 (2019-10-24)

**Features**

  - Model Domain has a new parameter input_schema
  - Model Domain has a new parameter input_schema_mapping
  - Model Domain has a new parameter metric_resource_id
  - Model EventSubscription has a new parameter event_delivery_schema
  - Model Topic has a new parameter input_schema
  - Model Topic has a new parameter input_schema_mapping
  - Model Topic has a new parameter metric_resource_id
  - Model WebHookEventSubscriptionDestination has a new parameter
    preferred_batch_size_in_kilobytes
  - Model WebHookEventSubscriptionDestination has a new parameter
    azure_active_directory_application_id_or_uri
  - Model WebHookEventSubscriptionDestination has a new parameter
    max_events_per_batch
  - Model EventSubscriptionUpdateParameters has a new parameter
    event_delivery_schema

**General Breaking Changes**

This version uses a next-generation code generator that *might*
introduce breaking changes. In summary, some modules were incorrectly
visible/importable and have been renamed. This fixed several issues
caused by usage of classes that were not supposed to be used in the
first place.

  - EventGridManagementClient cannot be imported from
    `azure.mgmt.eventgrid.event_grid_management_client` anymore
    (import from `azure.mgmt.eventgrid` works like before)
  - EventGridManagementClientConfiguration import has been moved from
    `azure.mgmt.eventgrid.event_grid_management_client` to
    `azure.mgmt.eventgrid`
  - A model `MyClass` from a "models" sub-module cannot be imported
    anymore using `azure.mgmt.eventgrid.models.my_class` (import from
    `azure.mgmt.eventgrid.models` works like before)
  - An operation class `MyClassOperations` from an `operations`
    sub-module cannot be imported anymore using
    `azure.mgmt.eventgrid.operations.my_class_operations` (import
    from `azure.mgmt.eventgrid.operations` works like before)

Last but not least, HTTP connection pooling is now enabled by default.
You should always use a client as a context manager, or call close(), or
use no more than one client per process.

## 2.1.0 (2019-05-22)

Not all preview features of the 2.1.0rc1 were confirmed in this 2.1.0
stable version. In particular, the following features will still be
available only in the 2.1.0rc1 for now:

  - Input mapping/Delivery Schema.
  - "label" filtering parameter in all operations

All other features are now considerd stable to use in production. This
includes:

  - Domains, which include all domain related operation including
    adding/deleting domain topics manually.
  - Pagination/filtering
  - Servicebus queue as destination
  - Advanced filtering, which was introduced in previous preview
    version.
  - Showing and selecting default event types instead of ‘all’

## 2.1.0rc1 (2019-03-11)

**Disclaimer**

Preview features that were on 2.0.0rc2 only and not on 2.0.0 has been
ported in this version.

This version also adds the following preview features: - Manual
Add/delete of domain topics. - Pagination/search filtering for list
operations. - Adding service bus queue as destination

## 2.0.0 (2019-02-01)

**Disclaimer**

Not all preview features of the 2.0.0rc2 were confirmed in this 2.0.0
stable version. In particular, the following features will still be
available only in the 2.0.0rc2 for now:

  - Domains.
  - Advanced filters support.
  - Event subscription expiration date
  - Input mapping and event delivery schema.

All other features are now considerd stable to use in production. This
includes:

  - Deadletter destination.
  - Storage queue as destination.
  - Hybrid connection as destination.
  - Retry policy.
  - Manual handshake.

## 2.0.0rc2 (2018-10-24)

**Features**

  - Model EventSubscriptionFilter has a new parameter advanced_filters
  - Model EventSubscriptionUpdateParameters has a new parameter
    expiration_time_utc
  - Model EventSubscription has a new parameter expiration_time_utc
  - Added operation EventSubscriptionsOperations.list_by_domain_topic
  - Added operation group DomainTopicsOperations
  - Added operation group DomainsOperations

Internal API version is 2018-09-15-preview

## 2.0.0rc1 (2018-05-04)

**Features**

  - input mappings for topics
  - CloudEvents support for topics
  - customizable delivery schemas
  - delivering events to Azure Storage queue and Azure hybrid
    connections
  - deadlettering
  - retry policies
  - manual subscription validation handshake validation.

Internal API version is 2018-05-01-preview

## 1.0.0 (2018-04-26)

**General Breaking changes**

This version uses a next-generation code generator that *might*
introduce breaking changes.

  - Model signatures now use only keyword-argument syntax. All
    positional arguments must be re-written as keyword-arguments. To
    keep auto-completion in most cases, models are now generated for
    Python 2 and Python 3. Python 3 uses the "*" syntax for
    keyword-only arguments.
  - Enum types now use the "str" mixin (class AzureEnum(str, Enum)) to
    improve the behavior when unrecognized enum values are encountered.
    While this is not a breaking change, the distinctions are important,
    and are documented here:
    <https://docs.python.org/3/library/enum.html#others> At a glance:
      - "is" should not be used at all.
      - "format" will return the string value, where "%s" string
        formatting will return `NameOfEnum.stringvalue`. Format syntax
        should be prefered.
  - New Long Running Operation:
      - Return type changes from
        `msrestazure.azure_operation.AzureOperationPoller` to
        `msrest.polling.LROPoller`. External API is the same.
      - Return type is now **always** a `msrest.polling.LROPoller`,
        regardless of the optional parameters used.
      - The behavior has changed when using `raw=True`. Instead of
        returning the initial call result as `ClientRawResponse`,
        without polling, now this returns an LROPoller. After polling,
        the final resource will be returned as a `ClientRawResponse`.
      - New `polling` parameter. The default behavior is
        `Polling=True` which will poll using ARM algorithm. When
        `Polling=False`, the response of the initial call will be
        returned without polling.
      - `polling` parameter accepts instances of subclasses of
        `msrest.polling.PollingMethod`.
      - `add_done_callback` will no longer raise if called after
        polling is finished, but will instead execute the callback right
        away.

**Features**

  - Client class can be used as a context manager to keep the underlying
    HTTP session open for performance

## 0.4.0 (2018-01-16)

**Breaking changes**

  - EventSubscription create is renamed to create_or_update.
  - Regenerated SDK based on 2018-01-01 API version.
  - OperationOrigin enum is removed. Origin of the operation is now a
    string.

## 0.3.0 (2017-11-02)

**Features**

  - Support for updating Topic properties

## 0.2.0 (2017-09-13)

**Breaking changes**

  - Use WebHookEventSubscriptionDestination for webhook endpoint URLs.
  - Regenerated based on 2017-09-15-preview version

## 0.1.1 (2017-08-17)

**Bugfixes**

  - Fix unexpected exception in some delete call

## 0.1.0 (2017-08-17)

  - Initial Release
