from rest_framework import serializers
from .models import WarehouseOrder


class WarehouseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseOrder
        fields = ('id', 'product_name', 'quantity', 'status')
