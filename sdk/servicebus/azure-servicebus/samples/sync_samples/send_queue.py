#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""
Example to show sending message(s) to a Service Bus Queue.
"""

import os
from azure.servicebus import ServiceBusClient, ServiceBusMessage, TransportType


CONNECTION_STR = os.environ['SERVICEBUS_CONNECTION_STR']
QUEUE_NAME = os.environ["SERVICEBUS_QUEUE_NAME"]

import logging
import sys
handler = logging.StreamHandler(stream=sys.stdout)
logger = logging.getLogger('azure.servicebus')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)
uamqp_logger = logging.getLogger('uamqp')
uamqp_logger.setLevel(logging.DEBUG)
uamqp_logger.addHandler(handler)

def send_single_message(sender):
    message = ServiceBusMessage("Single Message")
    sender.send_messages(message)
    print('send')


def send_a_list_of_messages(sender):
    messages = [ServiceBusMessage("Message in list") for _ in range(10)]
    sender.send_messages(messages)


def send_batch_message(sender):
    batch_message = sender.create_message_batch()
    for _ in range(10):
        try:
            batch_message.add_message(ServiceBusMessage("Message inside a ServiceBusMessageBatch"))
        except ValueError:
            # ServiceBusMessageBatch object reaches max_size.
            # New ServiceBusMessageBatch object can be created here to send more data.
            break
    sender.send_messages(batch_message)


servicebus_client = ServiceBusClient.from_connection_string(
    conn_str=CONNECTION_STR,
    logging_enable=True,
    transport_type=TransportType.Amqp,
    #uamqp_transport=True
)
with servicebus_client:
    sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
    with sender:
        while True:
            send_single_message(sender)
        #send_a_list_of_messages(sender)
        #send_batch_message(sender)

print("Send message is done.")
