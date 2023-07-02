import requests
from loguru import logger
from django.conf import settings


def create_or_update_warehouse_order(instance, created):
    data = {
        'id': str(instance.id),
        'product_name': instance.product_name,
        'quantity': instance.quantity,
        'status': instance.status
    }
    try:
        if created:
            response = requests.post(f'{settings.DJANGO_HOST}/api/v1/warehouse-orders/', data=data)
            response.raise_for_status()
        else:
            response = requests.put(f'{settings.DJANGO_HOST}/api/v1/warehouse-orders/{instance.id}/', data=data)
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f'Request failed: {e}')


def delete_warehouse_order(instance):
    try:
        response = requests.delete(f'{settings.DJANGO_HOST}/api/v1/warehouse-orders/{instance.id}/')
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f'Request failed: {e}')
