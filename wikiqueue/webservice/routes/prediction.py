from pydantic import BaseModel

from fastapi import APIRouter, Depends
from starlette.requests import Request

from ..core import security
from ..core.messages import NO_VALID_PAYLOAD

router = APIRouter()


class PredictionRequest(BaseModel):
    value: int


@router.post("/predict", name="predict")
def post_predict(
    request: Request,
    authenticated: bool = Depends(security.validate_request),
    prediction_request: PredictionRequest = None,
) -> int:
    if prediction_request is None:
        raise ValueError(NO_VALID_PAYLOAD.format(prediction_request))
    return prediction_request.value + 1
