import uuid

from django.db import models


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

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'warehouse_order'
        app_label = 'warehouse'
