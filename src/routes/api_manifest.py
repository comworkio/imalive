from fastapi import APIRouter
from fastapi.responses import JSONResponse

from utils.otel import get_otel_tracer
from utils.manifests import get_manifest_as_dict

router = APIRouter()

@router.get("")
def get_manifest():
    with get_otel_tracer().start_as_current_span("imalive-manifest-route"):
        manifest = get_manifest_as_dict()

        if manifest['status'] == 'error':
            return JSONResponse(content=manifest, status_code=500)
        else:
            return manifest
