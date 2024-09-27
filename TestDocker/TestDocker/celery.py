from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestDocker.settings')

# Create a new Celery app
app = Celery('TestDocker')

# Load the settings from the Django settings module
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks.py files in your apps
app.autodiscover_tasks()
