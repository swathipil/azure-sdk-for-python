#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""
Example to show iterator receiving from a Service Bus Queue.
"""

import threading
from datetime import datetime
import os
import time
import concurrent
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from azure.servicebus.management import ServiceBusAdministrationClient
import logging
import sys

# The logging levels below may need to be changed based on the logging that you want to suppress.
uamqp_logger = logging.getLogger('uamqp')
uamqp_logger.setLevel(logging.DEBUG)

# Configure a console output
#handler = logging.StreamHandler(stream=sys.stdout)
#uamqp_logger.addHandler(handler)

CONNECTION_STR = os.environ['SERVICE_BUS_CONNECTION_STR']
QUEUE_NAME = os.environ["SERVICE_BUS_QUEUE_NAME"]

mgmt_client = ServiceBusAdministrationClient.from_connection_string(CONNECTION_STR, logging_enable=True)
queue_runtime_properties = mgmt_client.get_queue_runtime_properties(QUEUE_NAME)
print("Message Count:", queue_runtime_properties.total_message_count)
print("Active Message Count:", queue_runtime_properties.active_message_count)

NUM_MESSAGES = 2000
UPDATE_INTERVAL = 10
EXCEPTION = False
sb_client = ServiceBusClient.from_connection_string(
    CONNECTION_STR, logging_enable=True)
sender = sb_client.get_queue_sender(QUEUE_NAME)
batch_message = sender.create_message_batch()
for i in range(NUM_MESSAGES):
    try:
        batch_message.add_message(ServiceBusMessage(b"a" * 1024))
    except ValueError:
        # ServiceBusMessageBatch object reaches max_size.
        # New ServiceBusMessageBatch object can be created here to send more data.
        sender.send_messages(batch_message)
        batch_message = sender.create_message_batch()
sender.send_messages(batch_message)
time.sleep(10)
queue_runtime_properties = mgmt_client.get_queue_runtime_properties(QUEUE_NAME)
print("Message Count:", queue_runtime_properties.total_message_count)
print("Active Message Count:", queue_runtime_properties.active_message_count)
def receive():
    schedule_update_queue()
    try:
        receiver = sb_client.get_queue_receiver(QUEUE_NAME)
        msgs_received = {}
        with receiver:
            for msg in receiver:
                print(msg.sequence_number)
                num = msg.sequence_number
                if num in msgs_received:
                    print(f'duplicate msg:{num}')
                msgs_received[num] = 1
                receiver.complete_message(msg)

                if len(msgs_received) == NUM_MESSAGES:
                    print('all messages received')
                    EXCEPTION = True
                    #proc_pool.shutdown(wait=False, cancel_futures=True)
                    break
            print('outside for')
        print('outside with')
    except Exception as e:
        print('hit an exception need to kill program')
        print(e)
        EXCEPTION = True
        #sb_client.close()
        #servicebus_mgmt_client.close()
    print('after both')

def schedule_update_queue():
    def _update_queue_properties():
        if not EXCEPTION:
            queue_properties = mgmt_client.get_queue(QUEUE_NAME)
            if queue_properties.max_delivery_count == 10:
                queue_properties.max_delivery_count = 11
            else:
                queue_properties.max_delivery_count = 10
            mgmt_client.update_queue(queue_properties)
            print("Updating queue.")
    t = threading.Timer(UPDATE_INTERVAL, _update_queue_properties)
    t.start()

def update_queue():
    while True:
        queue_properties = mgmt_client.get_queue(QUEUE_NAME)
        if queue_properties.max_delivery_count == 10:
            queue_properties.max_delivery_count = 11
        else:
            queue_properties.max_delivery_count = 10
        mgmt_client.update_queue(queue_properties)
        print("Updating queue.")
        time.sleep(30)

print('start receiving')
with sb_client:
    receive()
print('end receive')
