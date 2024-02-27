from fastapi import APIRouter

from main import OTEL_TRACER
from utils.metrics import all_metrics

router = APIRouter()

@router.get("")
def get_metrics():
    with OTEL_TRACER.start_as_current_span("imalive-metrics-route"):
        return all_metrics()
