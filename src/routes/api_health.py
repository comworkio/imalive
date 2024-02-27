from fastapi import APIRouter

from utils.otel import get_otel_tracer
from utils.health import health

router = APIRouter()

@router.get("")
def get_health():
    with get_otel_tracer().start_as_current_span("imalive-health-get-route"):
        return health()

@router.post("")
def post_health():
    with get_otel_tracer().start_as_current_span("imalive-health-post-route"):
        return health()
