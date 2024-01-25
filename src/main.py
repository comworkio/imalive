import os

from fastapi import FastAPI
from multiprocessing import Process
from utils.heartbit import heartbit
from restful_ressources import import_ressources

app = FastAPI(
    docs_url="/docs",
    title="Imalive API Documentation",
    version = os.environ['APP_VERSION'],
    description="Official Iamalive API Swagger documentation"
)

async_process = Process( 
    target=heartbit,
    daemon=True
)
async_process.start()

import_ressources(app)
