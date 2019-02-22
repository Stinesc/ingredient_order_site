import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ingredient_order_site.settings')

app = Celery('ingredient_order_site')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check-orders-every-minute': {
        'task': 'foodprod.tasks.task_orders_deactivate',
        'schedule': crontab(),
    },
}
