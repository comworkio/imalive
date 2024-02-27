from fastapi import APIRouter

from main import OTEL_TRACER
from utils.health import health

router = APIRouter()

@router.get("/")
def get_root():
    with OTEL_TRACER.start_as_current_span("imalive-root-route"):
        return health()
