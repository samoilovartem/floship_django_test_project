from rest_framework import serializers
from .models import WarehouseOrder


class WarehouseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseOrder
        fields = ('product_name', 'quantity', 'status')
