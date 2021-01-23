from fastapi import APIRouter

from . import hearthbeat, prediction

api_router = APIRouter()
api_router.include_router(hearthbeat.router, tags=["health"], prefix="/health")
api_router.include_router(prediction.router, tags=["prediction"], prefix="/prediction")
