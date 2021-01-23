from dataclasses import dataclass
from fastapi import APIRouter, Depends
from starlette.requests import Request

from ..core import security

router = APIRouter()


@dataclass
class PredictionRequest:
    value: int


@router.post("/predict", name="predict")
def post_predict(
    request: Request,
    authenticated: bool = Depends(security.validate_request),
    prediction_request: PredictionRequest = None
) -> int:
    return prediction_request.value + 1
