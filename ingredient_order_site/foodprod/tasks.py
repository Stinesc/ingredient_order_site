from celery import task
from celery.utils.log import get_task_logger
from .models import Order
from django.utils import timezone
from django.template import Template, Context

logger = get_task_logger(__name__)


@task(bind=True)
def task_orders_deactivate(self):
    orders = Order.objects.filter(is_active=True)
    for order in orders:
        if (order.creation_datetime + timezone.timedelta(hours=1)) <= timezone.now():
            order.is_active = False
            order.save()
            logger.info(f'Order #{order.id} is deactivated')


REPORT_TEMPLATE = """
{% for order in orders %}
Order #{{ order.id }} was created {{ order.creation_datetime }}.
{% endfor %}
"""


@task(bind=True)
def generate_reports(self):
    orders = Order.objects.filter(creation_datetime__gte=timezone.now()-timezone.timedelta(days=7))
    if orders:
        template = Template(REPORT_TEMPLATE)
        with open('reports/report.txt', 'a') as f:
            f.write(template.render(context=Context({'orders': orders})))
