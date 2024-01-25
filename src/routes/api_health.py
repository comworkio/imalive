from utils.health import health
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_health():
    return health();

@router.post("/")
def post_health():
    return health();