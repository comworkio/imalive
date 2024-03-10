from uuid import uuid4
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exception_handlers import http_exception_handler
from asgi_correlation_id import CorrelationIdMiddleware, correlation_id
from prometheus_fastapi_instrumentator import Instrumentator
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from restful_ressources import import_ressources
from exception.ImaliveHTTPException import ImaliveHTTPException

from utils.common import is_not_empty
from utils.cid import get_current_cid
from utils.manifests import get_manifest_as_dict
from utils.heartbit import heartbit
from utils.otel import init_otel_tracer, init_otel_metrics

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

app.add_middleware(
    CorrelationIdMiddleware,
    header_name = 'x-imalive-cid',
    generator = lambda: "{}".format(uuid4())
)

instrumentator = Instrumentator()

init_otel_tracer()
init_otel_metrics()

heartbit()

instrumentator.instrument(app, metric_namespace='imalive', metric_subsystem='imalive')
instrumentator.expose(app, endpoint='/v1/prom')
instrumentator.expose(app, endpoint='/prom')

FastAPIInstrumentor.instrument_app(app)

@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    headers = {'x-imalive-cid': get_current_cid()}

    if isinstance(exc, ImaliveHTTPException):
        return JSONResponse(content = exc.message, status_code = exc.status_code, headers = headers)
    return await http_exception_handler(request, HTTPException(500, 'Internal server error', headers = headers))

import_ressources(app)
