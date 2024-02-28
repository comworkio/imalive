import os

from opentelemetry import trace
from opentelemetry.metrics import set_meter_provider, get_meter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.semconv.resource import ResourceAttributes
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter

from utils.common import is_enabled

_otel_tracer = trace.get_tracer(__name__)
_otel_collector_endpoint = os.getenv('OTEL_COLLECTOR_ENDPOINT')
_otel_service_name = "imalive-{}".format(os.getenv('IMALIVE_NODE_NAME', "anode"))
_otel_service_version = os.getenv('VERSION', '0.1')
_otel_meter = get_meter(_otel_service_name, version=_otel_service_version)
_otel_resource = Resource.create(attributes={
    ResourceAttributes.SERVICE_NAME: _otel_service_name,
})

def init_otel_tracer():
    trace.set_tracer_provider(TracerProvider(resource=_otel_resource))

    if is_enabled(_otel_collector_endpoint):
        trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=_otel_collector_endpoint, insecure=True)))

def init_otel_metrics():
    if is_enabled(_otel_collector_endpoint):
        otlp_exporter = OTLPMetricExporter(endpoint=_otel_collector_endpoint, insecure=True)
        set_meter_provider(MeterProvider(resource=_otel_resource, metric_readers=[PeriodicExportingMetricReader(otlp_exporter, export_interval_millis=5000)]))

def get_otel_tracer():
    return _otel_tracer

def get_otel_meter():
    return _otel_meter
