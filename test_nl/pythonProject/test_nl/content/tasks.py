from celery import shared_task
from django.db.models import F
from .models import Page

@shared_task
def increment_counter(page_id):
    Page.objects.filter(id=page_id).update(counter=F('counter') + 1)