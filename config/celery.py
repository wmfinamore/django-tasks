import os
from datetime import timedelta
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')

app.conf.enable_utc = False

app.conf.update(timezone='America/Sao_Paulo')

app.config_from_object('django.conf::settings', namespace='CELERY')

app.autodiscover_tasks()

# Tasks will be named, and configured here
app.conf.beat_schedule = {}
