import json
from pydantic import BaseModel
from fastapi import APIRouter
from ..celery.worker import celery


class Item(BaseModel):
    value: int


router = APIRouter()


@router.post("/task", name="worker")
async def creat_item(item: Item):
    task_name = "prediction.task"
    task = celery.send_task(task_name, args=[item.value])
    return {
        'id': task.id,
        'url': f'localhost:8000/worker/check_task/{task.id}'
    }


@router.get("/check_task/{id}")
def check_task(id: str):
    task = celery.AsyncResult(id)
    if task.state == 'SUCCESS':
        response = {
            'status': task.state,
            'result': task.result,
            'task_id': id
        }
    elif task.state == 'FAILURE':
        response = json.loads(task.backend.get(task.backend.get_key_for_task(task.id)).decode('utf-8'))
        del response['children']
        del response['traceback']
    else:
        response = {
            'status': task.state,
            'result': task.info,
            'task_id': id
        }
    return response
