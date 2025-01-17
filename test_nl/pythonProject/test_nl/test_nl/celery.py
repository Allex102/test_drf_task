from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_nl.settings')

celery_app = Celery('test_nl')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')

celery_app.autodiscover_tasks()