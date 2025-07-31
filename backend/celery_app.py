from celery import Celery, Task
from app import app

def make_celery(app):
    class FlaskTask(Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.config_from_object(app.config, namespace='CELERY')
    celery.Task = FlaskTask
    return celery

celery = make_celery(app)


