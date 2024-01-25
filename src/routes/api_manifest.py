import os
import json
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("")
def get_manifest():
    try:
        with open(os.environ['MANIFEST_FILE_PATH']) as manifest_file:
            manifest = json.load(manifest_file)
            return manifest
    except IOError as err:
        return JSONResponse(content={'status': 'error', 'reason': err}, status_code=500)
