import os

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

from utils.common import is_enabled

_otel_tracer = trace.get_tracer(__name__)
_otel_collector_url = os.getenv('OTEL_COLLECTOR_URL')

def init_otel_tracer():
    trace.set_tracer_provider(TracerProvider())
    if is_enabled(_otel_collector_url):
        trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=_otel_collector_url, insecure=True)))

def get_otel_tracer():
    return _otel_tracer
