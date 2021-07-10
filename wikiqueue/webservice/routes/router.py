from fastapi import APIRouter

from . import hearthbeat, prediction, worker

api_router = APIRouter()
api_router.include_router(hearthbeat.router, tags=["health"], prefix="/health")
api_router.include_router(prediction.router, tags=["prediction"], prefix="/prediction")
api_router.include_router(worker.router, tags=["worker"], prefix="/worker")
