# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.hybridcompute.aio import HybridComputeManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestHybridComputeManagementExtensionMetadataOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(HybridComputeManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_extension_metadata_get(self, resource_group):
        response = await self.client.extension_metadata.get(
            location="str",
            publisher="str",
            extension_type="str",
            version="str",
            api_version="2025-02-19-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_extension_metadata_list(self, resource_group):
        response = self.client.extension_metadata.list(
            location="str",
            publisher="str",
            extension_type="str",
            api_version="2025-02-19-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
