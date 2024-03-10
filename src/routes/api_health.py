from fastapi import APIRouter

from utils.cid import get_current_cid
from utils.counter import create_counter, increment_counter
from utils.otel import get_otel_tracer
from utils.health import health

router = APIRouter()
_counter = create_counter("health_api_counter", "Health API counter")

@router.get("")
def get_health():
    with get_otel_tracer().start_as_current_span("imalive-health-get-route"):
        increment_counter(_counter, get_current_cid())
        return health()

@router.post("")
def post_health():
    with get_otel_tracer().start_as_current_span("imalive-health-post-route"):
        increment_counter(_counter, get_current_cid())
        return health()
