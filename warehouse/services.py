import requests
from django.conf import settings
from loguru import logger


def create_or_update_store_order(instance, created):
    data = {
        'id': str(instance.id),
        'product_name': instance.product_name,
        'quantity': instance.quantity,
        'status': instance.status,
        'sync': False,
    }
    try:
        if created:
            response = requests.post(f'{settings.DJANGO_HOST}/api/v1/store-orders/', data=data)
            response.raise_for_status()
        else:
            response = requests.put(f'{settings.DJANGO_HOST}/api/v1/store-orders/{instance.id}/', data=data)
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f'Request failed: {e}')
