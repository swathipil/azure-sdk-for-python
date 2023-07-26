#!/bin/bash
set -ex

# If you see this error: `/bin/bash^M: bad interpreter: No such file or directory``
# Run the following to remove the `^M` characters:
# stress/scripts> $path = "checkpoint_eh_disable_test_async.sh"
# stress/scripts> (Get-Content $path -Raw).Replace("`r`n","`n") | Set-Content $path -Force

mkdir -p $DEBUG_SHARE

cat > $DEBUG_SHARE/output_producer.log
cat > $DEBUG_SHARE/output_consumer1.log

python azure_eventhub_consumer_stress_async.py \
    --duration 259200 \
    --storage_conn_str \
    --storage_container_name \
    --log_filename $DEBUG_SHARE/output_consumer1.log \
    --pyamqp_logging_enable \
    --eh_random_disable \
    --debug_level "Info" &

python azure_eventhub_producer_stress.py -m stress_send_list_async --duration 259200 --log_filename $DEBUG_SHARE/output_producer.log  --pyamqp_logging_enable --debug_level "Info"
