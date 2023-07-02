import requests

from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class StoreOrder(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
    )

    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'store_order'
        app_label = 'store'


@receiver(post_save, sender=StoreOrder)
def create_or_update_warehouse_order(sender, instance, created, **kwargs):
    data = {
        'product_name': instance.product_name,
        'quantity': instance.quantity,
        'status': instance.status
    }
    try:
        if created:
            response = requests.post('http://django:8000/api/v1/warehouse-orders/', data=data)
            response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx
        else:
            response = requests.put(f'http://django:8000/api/v1/warehouse-orders/{instance.id}/', data=data)
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')


@receiver(post_delete, sender=StoreOrder)
def delete_warehouse_order(sender, instance, **kwargs):
    try:
        response = requests.delete(f'http://django:8000/api/v1/warehouse-orders/{instance.id}/')
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')
