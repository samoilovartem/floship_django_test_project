import uuid

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from warehouse.services import create_or_update_store_order


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True


class WarehouseOrder(UUIDMixin):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
    )

    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    sync = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'warehouse_order'
        app_label = 'warehouse'


@receiver(post_save, sender=WarehouseOrder)
def handle_store_order_save(sender, instance, created, **kwargs):
    if instance.sync:
        create_or_update_store_order(instance, created)
