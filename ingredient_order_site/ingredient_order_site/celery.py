import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ingredient_order_site.settings')

app = Celery('ingredient_order_site',
             backend=os.getenv('CELERY_BACKEND', 'redis://redis:6379/0'),
             broker=os.getenv('CELERY_BROKER', 'redis://redis:6379/0'))
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check-orders-every-minute': {
        'task': 'foodprod.tasks.task_orders_deactivate',
        'schedule': crontab(),
    },
    'generate-report-every-week': {
        'task': 'foodprod.tasks.generate_reports',
        'schedule': crontab(day_of_week=1),
    },
}
