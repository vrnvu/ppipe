from fastapi import FastAPI

from .routes.router import api_router
from .core.config import APP_NAME, APP_VERSION, IS_DEBUG, API_PREFIX


def get_app() -> FastAPI:
    app = FastAPI(title=APP_NAME, version=APP_VERSION, debug=IS_DEBUG)
    app.include_router(api_router, prefix=API_PREFIX)
    return app


app = get_app()
