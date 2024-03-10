from fastapi import APIRouter

from utils.otel import get_otel_tracer
from utils.health import health
from utils.counter import create_counter, increment_counter
from utils.cid import get_current_cid

router = APIRouter()
_counter = create_counter("root_api_counter", "Root API counter")

@router.get("/")
def get_root():
    with get_otel_tracer().start_as_current_span("imalive-root-route"):
        increment_counter(_counter, get_current_cid())
        return health()
