from fastapi import APIRouter

router = APIRouter()


@router.get("/heartbeat", name="heartbeat")
def get_hearbeat():
    return {"is_alive": True}
