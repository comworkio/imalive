from fastapi import APIRouter

from utils.counter import create_counter, increment_counter
from utils.otel import get_otel_tracer
from utils.metrics import all_metrics

router = APIRouter()
_counter = create_counter("metrics_api_counter", "Health API counter")

@router.get("")
def get_metrics():
    with get_otel_tracer().start_as_current_span("imalive-metrics-route"):
        increment_counter(_counter)
        return all_metrics()
