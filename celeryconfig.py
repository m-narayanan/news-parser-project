# Broker settings
broker_url = 'redis://localhost:6379/0'

# Using Redis as the result backend as well
result_backend = 'redis://localhost:6379/1'

# List of modules to import when the Celery worker starts
imports = ('app.tasks',)

# Set up periodic tasks
from celery.schedules import crontab

beat_schedule = {
    'process-feeds-every-hour': {
        'task': 'app.tasks.process_feeds',
        'schedule': crontab(minute=0, hour='*/1'),
    },
}