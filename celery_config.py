from celery import Celery

CeleryTask = Celery('celery_config', broker='redis://localhost:6379/0', include=['tasks'])
