from rest_framework import viewsets

from warehouse.models import WarehouseOrder
from warehouse.serializers import WarehouseOrderSerializer


class WarehouseOrderViewSet(viewsets.ModelViewSet):
    queryset = WarehouseOrder.objects.all()
    serializer_class = WarehouseOrderSerializer
