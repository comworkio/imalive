import os
import json
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("")
def get_manifest():
    manifest = get_manifest()

    if manifest['status'] == 'error':
        return JSONResponse(content=manifest, status_code=500)
    else:
        return manifest
