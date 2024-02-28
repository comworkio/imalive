from fastapi import APIRouter

from utils.otel import get_otel_tracer
from utils.metrics import all_metrics

router = APIRouter()

@router.get("")
def get_metrics():
    with get_otel_tracer().start_as_current_span("imalive-metrics-route"):
        return all_metrics()
