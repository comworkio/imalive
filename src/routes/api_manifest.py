from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils.manifests import get_manifest_as_dict

router = APIRouter()

@router.get("")
def get_manifest():
    manifest = get_manifest_as_dict()

    if manifest['status'] == 'error':
        return JSONResponse(content=manifest, status_code=500)
    else:
        return manifest
