# pylint: disable=line-too-long,useless-suppression
#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""
FILE: eventhub_receive_integration_async.py
DESCRIPTION:
    Examples to show receiving events asynchronously from EventHub with JsonSchemaEncoder integrated for content decoding.
USAGE:
    python eventhub_receive_integration_async.py
    Set the environment variables with your own values before running the sample:
    1) AZURE_TENANT_ID - Required for use of the credential. The ID of the service principal's tenant.
     Also called its 'directory' ID.
    2) AZURE_CLIENT_ID - Required for use of the credential. The service principal's client ID.
     Also called its 'application' ID.
    3) AZURE_CLIENT_SECRET - Required for use of the credential. One of the service principal's client secrets.
    4) SCHEMAREGISTRY_JSON_FULLY_QUALIFIED_NAMESPACE - The schema registry fully qualified namespace,
     which should follow the format: `<your-namespace>.servicebus.windows.net`
    5) SCHEMAREGISTRY_GROUP - The name of the JSON schema group.
    6) EVENT_HUB_CONN_STR - The connection string of the Event Hubs namespace to receive events from.
    7) EVENT_HUB_NAME - The name of the Event Hub in the Event Hubs namespace to receive events from.

This example uses DefaultAzureCredential, which requests a token from Azure Active Directory.
For more information on DefaultAzureCredential, see
    https://learn.microsoft.com/python/api/azure-identity/azure.identity.aio.defaultazurecredential?view=azure-python
"""
import os
import asyncio
from azure.eventhub.aio import EventHubConsumerClient
from azure.identity.aio import DefaultAzureCredential
from azure.schemaregistry.aio import SchemaRegistryClient
from azure.schemaregistry.encoder.jsonencoder.aio import JsonSchemaEncoder

EVENTHUB_CONNECTION_STR = os.environ["EVENT_HUB_CONN_STR"]
EVENTHUB_NAME = os.environ["EVENT_HUB_NAME"]

SCHEMAREGISTRY_FULLY_QUALIFIED_NAMESPACE = os.environ["SCHEMAREGISTRY_JSON_FULLY_QUALIFIED_NAMESPACE"]
GROUP_NAME = os.environ["SCHEMAREGISTRY_GROUP"]
META_SCHEMA_IDENTIFIER = "https://json-schema.org/draft/2020-12/schema"


# create an EventHubConsumerClient instance
eventhub_consumer = EventHubConsumerClient.from_connection_string(
    conn_str=EVENTHUB_CONNECTION_STR,
    consumer_group="$Default",
    eventhub_name=EVENTHUB_NAME,
)
# create a JsonSchemaEncoder instance
azure_credential = DefaultAzureCredential()
json_schema_encoder = JsonSchemaEncoder(
    client=SchemaRegistryClient(
        fully_qualified_namespace=SCHEMAREGISTRY_FULLY_QUALIFIED_NAMESPACE, credential=azure_credential
    ),
    validate=META_SCHEMA_IDENTIFIER,
)


async def on_event(partition_context, event):
    print(f"Received event from partition: {partition_context.partition_id}.")

    bytes_payload = b"".join(b for b in event.body)
    print(f"The received bytes of the EventData is {bytes_payload!r}.")

    # Use the decode method to decode the payload of the event.
    # The decode method will extract the schema id from the content_type, and automatically retrieve the Json Schema
    # from the Schema Registry Service. The schema will be cached locally for future usage.
    decoded_content = await json_schema_encoder.decode(event)
    print(f"The dict content after decoding is {decoded_content}")


async def main():
    try:
        async with eventhub_consumer, json_schema_encoder:
            await eventhub_consumer.receive(
                on_event=on_event,
                starting_position="-1",  # "-1" is from the beginning of the partition.
            )
    except KeyboardInterrupt:
        print("Stopped receiving.")
    finally:
        await json_schema_encoder.close()
        await azure_credential.close()
        await eventhub_consumer.close()


if __name__ == "__main__":
    asyncio.run(main())
