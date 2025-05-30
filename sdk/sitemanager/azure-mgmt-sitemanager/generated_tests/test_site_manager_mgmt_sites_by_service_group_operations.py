# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.sitemanager import SiteManagerMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSiteManagerMgmtSitesByServiceGroupOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(SiteManagerMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_sites_by_service_group_list_by_service_group(self, resource_group):
        response = self.client.sites_by_service_group.list_by_service_group(
            servicegroup_name="str",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_sites_by_service_group_get(self, resource_group):
        response = self.client.sites_by_service_group.get(
            servicegroup_name="str",
            site_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_sites_by_service_group_begin_create_or_update(self, resource_group):
        response = self.client.sites_by_service_group.begin_create_or_update(
            servicegroup_name="str",
            site_name="str",
            resource={
                "id": "str",
                "name": "str",
                "properties": {
                    "description": "str",
                    "displayName": "str",
                    "labels": {"str": "str"},
                    "provisioningState": "str",
                    "siteAddress": {
                        "city": "str",
                        "country": "str",
                        "postalCode": "str",
                        "stateOrProvince": "str",
                        "streetAddress1": "str",
                        "streetAddress2": "str",
                    },
                },
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "type": "str",
            },
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_sites_by_service_group_update(self, resource_group):
        response = self.client.sites_by_service_group.update(
            servicegroup_name="str",
            site_name="str",
            properties={
                "properties": {
                    "description": "str",
                    "displayName": "str",
                    "labels": {"str": "str"},
                    "siteAddress": {
                        "city": "str",
                        "country": "str",
                        "postalCode": "str",
                        "stateOrProvince": "str",
                        "streetAddress1": "str",
                        "streetAddress2": "str",
                    },
                }
            },
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_sites_by_service_group_delete(self, resource_group):
        response = self.client.sites_by_service_group.delete(
            servicegroup_name="str",
            site_name="str",
        )

        # please add some check logic here by yourself
        # ...
