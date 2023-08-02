#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""
FILE: eventhub_send_integration.py
DESCRIPTION:
    Examples to show sending events synchronously to EventHub with JsonSchemaEncoder integrated for content encoding.
USAGE:
    python eventhub_send_integration.py
    Set the environment variables with your own values before running the sample:
    1) AZURE_TENANT_ID - Required for use of the credential. The ID of the service principal's tenant.
     Also called its 'directory' ID.
    2) AZURE_CLIENT_ID - Required for use of the credential. The service principal's client ID.
     Also called its 'application' ID.
    3) AZURE_CLIENT_SECRET - Required for use of the credential. One of the service principal's client secrets.
    4) SCHEMAREGISTRY_FULLY_QUALIFIED_NAMESPACE - The schema registry fully qualified namespace,
     which should follow the format: `<your-namespace>.servicebus.windows.net`
    5) SCHEMAREGISTRY_GROUP - The name of the schema group.
    6) EVENT_HUB_CONN_STR - The connection string of the Event Hubs namespace to send events to.
    7) EVENT_HUB_NAME - The name of the Event Hub in the Event Hubs namespace to send events to.

This example uses DefaultAzureCredential, which requests a token from Azure Active Directory.
For more information on DefaultAzureCredential, see
 https://docs.microsoft.com/python/api/overview/azure/identity-readme?view=azure-python#defaultazurecredential.
"""
import os
import json
import jsonschema

from azure.eventhub import EventHubProducerClient, EventData
from azure.identity import DefaultAzureCredential
from azure.schemaregistry import SchemaRegistryClient
from azure.schemaregistry.encoder import JsonSchemaEncoder, InvalidContentError

EVENTHUB_CONNECTION_STR = os.environ['EVENT_HUB_CONN_STR']
EVENTHUB_NAME = os.environ['EVENT_HUB_NAME']

SCHEMAREGISTRY_FULLY_QUALIFIED_NAMESPACE = os.environ['SCHEMAREGISTRY_JSON_FULLY_QUALIFIED_NAMESPACE']
GROUP_NAME = os.environ['SCHEMAREGISTRY_GROUP']

PERSON_SCHEMA_JSON = {
    "$id": "https://example.com/person.schema.json",
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Person",
    "type": "object",
    "properties": {
        "username": {
            "type": "string",
            "description": "Username."
        },
        "email": {
            "type": "string",
            "description": "Email address."
        },
        "favorite_number": {
            "description": "Favorite number.",
            "type": "integer",
        }
    },
    "oneOf": [
        {"required": ["name"]},
        {"required": ["email"]}
    ]
}
PERSON_SCHEMA_STRING = json.dumps(PERSON_SCHEMA_JSON)

CAT_SCHEMA_JSON = {
    "$id": "https://example.com/cat.schema.json",
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Cat",
    "type": "object",
    "required": ["name", "favorite_toy"],
    "properties": {
        "name": {
            "type": "string",
            "description": "Cat's name."
        },
        "favorite_toy": {
            "type": "string",
            "description": "Favorite toy."
        }
    }
}
CAT_SCHEMA_STRING = json.dumps(CAT_SCHEMA_JSON)

DOG_SCHEMA_JSON = {
    "$id": "https://example.com/dog.schema.json",
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Dog",
    "type": "object",
    "required": ["name"],
    "properties": {
        "name": {
            "type": "string",
            "description": "Dog's name."
        },
        "favorite_food": {
            "type": "string",
            "description": "Favorite food."
        }
    }
}
DOG_SCHEMA_STRING = json.dumps(DOG_SCHEMA_JSON)

def pre_register_schema(
    schema_registry: SchemaRegistryClient,
    schema_definition: str,
    schema_name: str
):
    schema_properties = schema_registry.register_schema(
        group_name=GROUP_NAME,
        name=schema_name,
        definition=schema_definition,
        format="Json"
    )
    return schema_properties.id

# pre-register schemas to be used
schema_registry = SchemaRegistryClient(
    fully_qualified_namespace=SCHEMAREGISTRY_FULLY_QUALIFIED_NAMESPACE,
    credential=DefaultAzureCredential(),
)
person_schema_id = pre_register_schema(
    schema_registry, PERSON_SCHEMA_STRING, PERSON_SCHEMA_JSON['title']
)
cat_schema_id = pre_register_schema(
    schema_registry, CAT_SCHEMA_STRING, CAT_SCHEMA_JSON['title']
)
dog_schema_id = pre_register_schema(
    schema_registry, DOG_SCHEMA_STRING, DOG_SCHEMA_JSON['title']
)

####################### USAGE SAMPLE #############################
# create file to write invalid data
invalid_data_file = open("invalid_data.txt", "w")


def add_data_to_batch(encoder, event_data_batch, schema_id, data_list):
    for data in data_list:
        try:
            event_data = encoder.encode(
                content=data, schema_id=schema_id, message_type=EventData
            )

            event_data_batch.add(event_data=event_data)
        except InvalidContentError as exc:
            # if type error, check the type and try to convert
            # else, write invalid data to file
            if (
                isinstance(exc.__cause__, jsonschema.exceptions.ValidationError) and \
                exc.__cause__.validator == "type"
            ):
                property = exc.__cause__.path.pop() # ex: "favorite_number"
                try:
                    if exc.__cause__.validator_value == "integer":
                        # try to convert to integer
                        data[property] = int(data[property])
                    data_list.append(data)
                except:
                    # write to file
                    invalid_data_file.write(json.dumps(data) + "\n")
            else:
                # write invalid data to file
                invalid_data_file.write(json.dumps(data) + "\n")

# create a JsonSchemaEncoder/EventHubProducer instance
producer = EventHubProducerClient.from_connection_string(
    conn_str=EVENTHUB_CONNECTION_STR,
    eventhub_name=EVENTHUB_NAME
)

encoder = JsonSchemaEncoder(client=schema_registry)

person_data_list = [
    {"name": "Bob", "favorite_number": 7, "favorite_color": "red"},
    # incorrect type string, expected integer
    {"name": "Bob", "favorite_number": "7", "favorite_color": "red"},
    # invalid, included multiple oneOf properties
    {"name": "Bob", "favorite_number": 7, "email": "bob1@contoso.com"},
]

dog_data_list = [
    {"name": "Fido", "favorite_food": "bone"},
    {"name": "Fido", "favorite_food": "bone", "favorite_toy": "ball"},
]

cat_data_list = [
    {"name": "Whiskers", "favorite_toy": "mouse"},
    {"favorite_toy": "mouse"},  # missing property
]


# send multiple types of event data
with producer, encoder:
    event_data_batch = producer.create_batch()

    # add "person" data
    add_data_to_batch(encoder, event_data_batch, person_schema_id, person_data_list)

    print('Added person data to batch.')

    # add "cat" data
    add_data_to_batch(encoder, event_data_batch, cat_schema_id, cat_data_list)
    print('Added cat data to batch.')

    # add "dog" data
    add_data_to_batch(encoder, event_data_batch, dog_schema_id, dog_data_list)
    print('Added dog data to batch.')

    # invalid data written to file:
    # {"name": "Bob", "favorite_number": 7, "email": "bob1@contoso.com"}
    # {"favorite_toy": "mouse"}

    producer.send_batch(event_data_batch)
    print('Send is done.')
