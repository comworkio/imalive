import os

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.semconv.resource import ResourceAttributes

from utils.common import is_enabled

_otel_tracer = trace.get_tracer(__name__)
_otel_collector_endpoint = os.getenv('OTEL_COLLECTOR_ENDPOINT')
_otel_service_name = os.getenv('IMALIVE_NODE_NAME', "anode")

def init_otel_tracer():
    trace.set_tracer_provider(TracerProvider(resource=Resource.create(attributes={
        ResourceAttributes.SERVICE_NAME: "imalive-{}".format(_otel_service_name),
    })))

    if is_enabled(_otel_collector_endpoint):
        trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=_otel_collector_endpoint, insecure=True)))

def get_otel_tracer():
    return _otel_tracer
