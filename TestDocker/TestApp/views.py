from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .tasks import example_task

def run_task(request):
    # Call the Celery task in the background
    task = example_task.delay()

    # Return the task ID to track the task status if needed
    return JsonResponse({'status': 'Task started', 'task_id': task.id})
