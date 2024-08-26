from celery import Celery

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def collect_data():
    raise NotImplementedError('Not implemented yet')
