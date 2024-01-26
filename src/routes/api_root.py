from utils.health import health
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_root():
    return health()
