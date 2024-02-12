import asyncio

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from multiprocessing import Process

from restful_ressources import import_ressources

from utils.common import is_not_empty
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

import_ressources(app)
