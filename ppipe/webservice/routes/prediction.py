from fastapi import APIRouter, Depends
from starlette.requests import Request

from ..core import security

router = APIRouter()


@router.post("/predict", name="predict")
def post_predict(
    request: Request,
    authenticated: bool = Depends(security.validate_request),
) -> bool:
    return True
