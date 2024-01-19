from celery import Celery
from celery.schedules import crontab
from flask import current_app as ap
from db.database import Users,db


celery = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
    include=["app.tasks"],  
)

celery.conf.timezone = 'Asia/Kolkata'  

class ContextTask(celery.Task):
    def _call_(self, *args, **kwargs):
        with ap.app_context():
            return self.run(*args, **kwargs)