import os

from fastapi import FastAPI
from multiprocessing import Process

from restful_ressources import import_ressources

from utils.common import is_not_empty
from utils.manifests import get_manifest
from utils.heartbit import heartbit

version = "unkown"
manifest = get_manifest()

if "version" in manifest and is_not_empty(manifest['version']):
    version = manifest['version']

app = FastAPI(
    docs_url="/docs",
    title="Imalive API Documentation",
    version = version,
    description="Official Imalive API Swagger documentation"
)

async_process = Process( 
    target=heartbit,
    daemon=True
)
async_process.start()

import_ressources(app)
