from fastapi import APIRouter

from utils.otel import get_otel_tracer
from utils.health import health

router = APIRouter()

@router.get("/")
def get_root():
    with get_otel_tracer().start_as_current_span("imalive-root-route"):
        return health()
