from utils.metrics import all_metrics
from fastapi import APIRouter

router = APIRouter()

@router.get("")
def get_metrics():
    return all_metrics()
