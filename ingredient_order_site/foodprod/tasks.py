from celery import task
from celery.utils.log import get_task_logger
from .models import Order
from django.utils import timezone

logger = get_task_logger(__name__)


@task(bind=True)
def task_orders_deactivate(self):
    orders = Order.objects.filter(is_active=True)
    for order in orders:
        if (order.creation_datetime + timezone.timedelta(minutes=1)) <= timezone.now():
            order.is_active = False
            order.save()
            logger.info(f'Order #{order.id} is deactivated')
