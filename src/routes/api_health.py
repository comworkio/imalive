from fastapi import APIRouter

from main import OTEL_TRACER
from utils.health import health

router = APIRouter()

@router.get("")
def get_health():
    with OTEL_TRACER.start_as_current_span("imalive-health-get-route"):
        return health()

@router.post("")
def post_health():
    with OTEL_TRACER.start_as_current_span("imalive-health-post-route"):
        return health()
