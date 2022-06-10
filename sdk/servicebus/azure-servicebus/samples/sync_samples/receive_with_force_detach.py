#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""
Example to show iterator receiving from a Service Bus Queue.
"""

import os
import queue
import time
import concurrent
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from azure.servicebus.management import ServiceBusAdministrationClient

CONNECTION_STR = os.environ['SERVICE_BUS_CONNECTION_STR']
QUEUE_NAME = os.environ["SERVICE_BUS_QUEUE_NAME"]

#servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR)
#
#with servicebus_client:
#    receiver = servicebus_client.get_queue_receiver(queue_name=QUEUE_NAME)
#    with receiver:
#        for msg in receiver:
#            #print(str(msg.application_properties))
#            #print(str(msg))
#            receiver.complete_message(msg)
#
#print("Receive is done.")

servicebus_mgmt_client = ServiceBusAdministrationClient.from_connection_string(CONNECTION_STR)
queue_runtime_properties = servicebus_mgmt_client.get_queue_runtime_properties(QUEUE_NAME)
print("Message Count:", queue_runtime_properties.total_message_count)
print("Active Message Count:", queue_runtime_properties.active_message_count)

NUM_MESSAGES = 500
UPDATE_INTERVAL = 20
EXCEPTION = False
sb_client = ServiceBusClient.from_connection_string(
    CONNECTION_STR, logging_enable=True)
sender = sb_client.get_queue_sender(QUEUE_NAME)
batch_message = sender.create_message_batch()
for i in range(NUM_MESSAGES):
    try:
        batch_message.add_message(ServiceBusMessage(b"a" * 1024, application_properties={'num': i}))
    except ValueError:
        # ServiceBusMessageBatch object reaches max_size.
        # New ServiceBusMessageBatch object can be created here to send more data.
        sender.send_messages(batch_message)
        batch_message = sender.create_message_batch()
        break
sender.send_messages(batch_message)
def receive():
    try:
        receiver = sb_client.get_queue_receiver(QUEUE_NAME)
        msgs_received = {}
        with receiver:
            for msg in receiver:
                print(msg.application_properties.get(b'num'))
                num = msg.application_properties.get(b'num')
                if num in msgs_received:
                    EXCEPTION = True
                    print(f'duplicate msg:{num}')
                msgs_received[num] = 1
                receiver.complete_message(msg)

                if len(msgs_received) == NUM_MESSAGES:
                    print('all messages received')
                    EXCEPTION = True
                    exit()
                    break
            print('outside for')
        print('outside with')
    except Exception as e:
        print(e)
        EXCEPTION = True
        exit()

def updating_queue():
    while not EXCEPTION:
        time.sleep(UPDATE_INTERVAL)
        queue_properties = servicebus_mgmt_client.get_queue(QUEUE_NAME)
        if queue_properties.max_delivery_count == 10:
            queue_properties.max_delivery_count = 11
        else:
            queue_properties.max_delivery_count = 10
        servicebus_mgmt_client.update_queue(queue_properties)
        print('updating queue')

print('start receiving')
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as proc_pool:
    received = proc_pool.submit(receive)
    updated = proc_pool.submit(updating_queue)
    for each in concurrent.futures.as_completed([received]):
        each.result()
    exit()
