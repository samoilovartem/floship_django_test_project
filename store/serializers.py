from rest_framework import serializers
from .models import StoreOrder


class StoreOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreOrder
        fields = ('id', 'product_name', 'quantity', 'status')
