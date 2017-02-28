from celery_config import CeleryTask
from models import tndb

@CeleryTask.task
def get_db_record(name):
    return tndb.db.query('select * from records where Name=%s', name)

