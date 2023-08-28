import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTING_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespase='CELERY')
app.autodiscover_tasks()
