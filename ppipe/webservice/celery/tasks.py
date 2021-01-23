from time import sleep
import traceback

from celery import states

from .worker import celery


@celery.task(name='prediction.task', bind=True)
def hello_world(self, value):
    try:
        for i in range(60):
            sleep(1)
            self.update_state(state='PROGRESS', meta={'done': i, 'total': 60})
        return {"result": value + 1}
    except Exception as ex:
        self.update_state(
            state=states.FAILURE,
            meta={
                'exc_type': type(ex).__name__,
                'exc_message': traceback.format_exc().split('\n')
            })
        raise ex
