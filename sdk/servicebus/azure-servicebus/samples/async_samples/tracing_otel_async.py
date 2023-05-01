from contextlib import asynccontextmanager
import datetime
import logging.config
import os
from azure.core.tracing.ext.opentelemetry_span import OpenTelemetrySpan
from azure.core.settings import settings
from azure.servicebus import ServiceBusMessage
from azure.servicebus.aio import ServiceBusClient
# otel libs
from opentelemetry.sdk import resources  # type: ignore
from opentelemetry.sdk.trace import TracerProvider  # type: ignore
from opentelemetry import trace  # type: ignore
# unsued but can export to a collector
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter  # type: ignore
from opentelemetry.sdk.trace.export import BatchSpanProcessor  # type: ignore

### FIRST INSTALL:
# >pip install opentelemetry-exporter-otlp opentelemetry-sdk azure-core-tracing-opentelemetry
# >pip install azure-core==1.26.3

UAMQP_TRANSPORT = False
CONNECTION_STR = os.environ['SERVICEBUS_CONNECTION_STR']
QUEUE_NAME = os.environ["SERVICEBUS_QUEUE_NAME"]
tracer: trace.Tracer = trace.get_tracer(__name__)
logging.config.dictConfig({
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "default": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout"
        }
    },
    "loggers": {"": {"handlers": ["default"], "level": "INFO"}},
    "azure": {"handlers": ["default"], "level": "WARN"},
    "uamqp": {"handlers": ["default"], "level": "WARN"},
})

def setup_otel():
    # Declare OpenTelemetry as enabled tracing plugin for Azure SDKs
    settings.tracing_implementation = OpenTelemetrySpan
    # Service name is required for most backends
    resource = resources.Resource(
        attributes={
            resources.DEPLOYMENT_ENVIRONMENT: "local",
            resources.SERVICE_NAME: "service-bus-otel-test",
            resources.SERVICE_VERSION: "0.0.1",
        }
    )
    # Set up traces provider
    provider = TracerProvider(resource=resource)
    
    # Can export to a collector (unnecessary for this demo)
    # processor = BatchSpanProcessor(
    #     OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
    # )
    # provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)

@asynccontextmanager
async def start_span(
    tracer: trace.Tracer,
    name: str,
):
    """
    Adds Parent Span information from `diagnostic_id` if otel enabled.
    """
    with tracer.start_as_current_span(
        name, kind=trace.SpanKind.CONSUMER
    ) as current_span:
        yield current_span

async def on_receive(msg: str):
    async with start_span(tracer, "service-bus-otel-test") as span:
        debug = f"MSG RECEIVED [{msg}] at {datetime.datetime.utcnow()}"
        print(debug)

async def receiver():
    servicebus_client = ServiceBusClient.from_connection_string(
    conn_str=CONNECTION_STR, uamqp_transport=UAMQP_TRANSPORT)
    async with servicebus_client:
        receiver = servicebus_client.get_queue_receiver(queue_name=QUEUE_NAME)
        async with receiver:
            async for msg in receiver:
                await on_receive(msg)
                await receiver.complete_message(msg)

async def sender(msg: str, delay: int):
    """
        msg: message to send
        delay: seconds to delay delivery
    """
    message = ServiceBusMessage(msg)
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    scheduled_time_utc = now + datetime.timedelta(seconds=delay)
    servicebus_client = ServiceBusClient.from_connection_string(
    conn_str=CONNECTION_STR, uamqp_transport=UAMQP_TRANSPORT)
    async with servicebus_client:
        sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
        async with sender:
            #await sender.schedule_messages([message], scheduled_time_utc)
            await sender.send_messages([message])

async def main(args):
    setup_otel()
    if args.send:
        msg = args.send
        assert bool(msg), "Message is not empty"
        debug = f"SENDING MESSAGE [{msg}] WITH DELAY {args.delay} at {datetime.datetime.utcnow()}"
        print(debug)
        await sender(msg, delay=args.delay)
    else:
        print("STARTING RECEIVER")
        await receiver()

if __name__ == "__main__":
    # TO SEND:
    # $ python service-bus-otel-test.py -s test20 -d 20
    # TO RECEIVE:
    # $ python service-bus-otel-test.py -r
    import argparse
    import asyncio
    parser = argparse.ArgumentParser("Azure Queues Test")
    parser.add_argument("-s", "--send", type=str, help="Send value into the queue")
    parser.add_argument("-d", "--delay", type=int, help="Message delay", default=0)
    parser.add_argument("-r", "--receiver", action="store_true", help="run receiver")
    args = parser.parse_args()
    asyncio.run(main(args))
