# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import threading
import time

from azure.eventhub import EventHubConsumerClient


CONNECTION_STR = os.environ['EVENT_HUB_CONN_STR_NEU_BASIC']
EVENTHUB_NAME = os.environ['EVENT_HUB_NAME']


def test_receive_fixed_time_interval():

    consumer_client = EventHubConsumerClient.from_connection_string(CONNECTION_STR, consumer_group="$Default", eventhub_name=EVENTHUB_NAME)

    last_received_count = [0]
    received_count = [0]
    run_flag = [True]
    all_perf_records = []
    check_interval = 5
    run_duration = 120

    def on_event(partition_context, event):
        received_count[0] += 1

    def monitor():
        while run_flag[0]:
            snap = received_count[0]
            perf = (snap - last_received_count[0]) / check_interval
            last_received_count[0] = snap
            all_perf_records.append(perf)
            time.sleep(check_interval)

    thread = threading.Thread(
        target=consumer_client.receive,
        kwargs={
            "on_event": on_event,
            "partition_id": "0",
            "starting_position": "-1",  # "-1" is from the beginning of the partition.
        }
    )

    monitor_thread = threading.Thread(
        target=monitor
    )

    thread.daemon = True
    monitor_thread.daemon = True

    thread.start()
    monitor_thread.start()
    time.sleep(run_duration)
    consumer_client.close()
    run_flag[0] = False

    valid_perf_records = all_perf_records[10:]  # skip the first 10 records to let the receiving program be stable
    avg_perf = sum(valid_perf_records) / len(valid_perf_records)
    print("The average performance is {} events/s".format(avg_perf))

def test_receive_fixed_amount():
    consumer_client = EventHubConsumerClient.from_connection_string(CONNECTION_STR, consumer_group="$Default", eventhub_name=EVENTHUB_NAME)
    run_times = 5
    fixed_amount = 50000
    perf_records = []
    received_count = [0]

    def on_event(partition_context, event):
        received_count[0] += 1
        if received_count[0] == fixed_amount:
            consumer_client.close()

    for i in range(run_times):
        start_time = time.time()
        with consumer_client:
            consumer_client.receive(
                on_event=on_event,
                partition_id="0",
                starting_position="-1"
            )
        end_time = time.time() 
        total_time = end_time - start_time
        speed = fixed_amount/total_time
        perf_records.append(speed)
        received_count[0] = 0
    avg_perf = sum(perf_records) / len(perf_records)
    print("perf_records: {}".format(perf_records))
    print("The average performance is {} event/s".format(avg_perf))
    


#test_receive_fixed_time_interval()
test_receive_fixed_amount()
