import os

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from restful_ressources import import_ressources

from utils.common import is_enabled, is_not_empty
from utils.manifests import get_manifest_as_dict
from utils.heartbit import heartbit

version = "unkown"
manifest = get_manifest_as_dict()

if "version" in manifest and is_not_empty(manifest['version']):
    version = manifest['version']

app = FastAPI(
    docs_url="/docs",
    title="Imalive API Documentation",
    version = version,
    description="Official Imalive API Swagger documentation"
)

instrumentator = Instrumentator()

heartbit()

instrumentator.instrument(app, metric_namespace='imalive', metric_subsystem='imalive')
instrumentator.expose(app, endpoint='/v1/prom')
instrumentator.expose(app, endpoint='/prom')

OTEL_COLLECTOR_URL = os.getenv('OTEL_COLLECTOR_URL')
trace.set_tracer_provider(TracerProvider())
OTEL_TRACER = trace.get_tracer(__name__)

if is_enabled(OTEL_COLLECTOR_URL):
    trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=OTEL_COLLECTOR_URL, insecure=True)))

FastAPIInstrumentor.instrument_app(app)

import_ressources(app)
