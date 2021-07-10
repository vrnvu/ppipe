from celery import Celery

from ..core.config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND


celery = Celery("worker", backend=CELERY_BROKER_URL, broker=CELERY_RESULT_BACKEND)
