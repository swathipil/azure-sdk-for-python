# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import AIProjectClientTestBase, AIProjectPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAIProjectIndexesOperations(AIProjectClientTestBase):
    @AIProjectPreparer()
    @recorded_by_proxy
    def test_indexes_list_versions(self, aiproject_endpoint):
        client = self.create_client(endpoint=aiproject_endpoint)
        response = client.indexes.list_versions(
            name="str",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @AIProjectPreparer()
    @recorded_by_proxy
    def test_indexes_list(self, aiproject_endpoint):
        client = self.create_client(endpoint=aiproject_endpoint)
        response = client.indexes.list()
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @AIProjectPreparer()
    @recorded_by_proxy
    def test_indexes_get(self, aiproject_endpoint):
        client = self.create_client(endpoint=aiproject_endpoint)
        response = client.indexes.get(
            name="str",
            version="str",
        )

        # please add some check logic here by yourself
        # ...

    @AIProjectPreparer()
    @recorded_by_proxy
    def test_indexes_delete(self, aiproject_endpoint):
        client = self.create_client(endpoint=aiproject_endpoint)
        response = client.indexes.delete(
            name="str",
            version="str",
        )

        # please add some check logic here by yourself
        # ...

    @AIProjectPreparer()
    @recorded_by_proxy
    def test_indexes_create_or_update(self, aiproject_endpoint):
        client = self.create_client(endpoint=aiproject_endpoint)
        response = client.indexes.create_or_update(
            name="str",
            version="str",
            body={
                "connectionName": "str",
                "indexName": "str",
                "name": "str",
                "type": "AzureSearch",
                "version": "str",
                "description": "str",
                "fieldMapping": {
                    "contentFields": ["str"],
                    "filepathField": "str",
                    "metadataFields": ["str"],
                    "titleField": "str",
                    "urlField": "str",
                    "vectorFields": ["str"],
                },
                "id": "str",
                "tags": {"str": "str"},
            },
        )

        # please add some check logic here by yourself
        # ...
