# Create your tasks here

from demoapp.models import Widget

from celery_file import shared_task


@shared_task
def add(x, y):
    return x + y
