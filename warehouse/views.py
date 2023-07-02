from rest_framework import viewsets

from .models import WarehouseOrder
from .serializers import WarehouseOrderSerializer


class WarehouseOrderViewSet(viewsets.ModelViewSet):
    queryset = WarehouseOrder.objects.all()
    serializer_class = WarehouseOrderSerializer
