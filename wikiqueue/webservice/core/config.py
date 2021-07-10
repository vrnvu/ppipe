from starlette.config import Config
from starlette.datastructures import Secret

APP_VERSION = "0.0.1"
APP_NAME = "wikiqueue fast api"
API_PREFIX = "/api"

config = Config(".env")

API_KEY: Secret = config("API_KEY", cast=Secret)
IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=False)

# Celery config
CELERY_BROKER_URL = config("REDISSERVER", cast=str, default="redis://redis_server:6379")
CELERY_RESULT_BACKEND = config(
    "REDISSERVER", cast=str, default="redis://redis_server:6379"
)
