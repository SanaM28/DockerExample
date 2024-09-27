import time
from celery import shared_task

@shared_task
def example_task():

    time.sleep(60)

    return "Task is executed!"
