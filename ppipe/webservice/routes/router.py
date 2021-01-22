from fastapi import APIRouter

from .hearthbeat import router

api_router = APIRouter()
api_router.include_router(router, tags=["health"], prefix="/health")
