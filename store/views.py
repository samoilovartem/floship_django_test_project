from rest_framework import viewsets

from store.models import StoreOrder
from store.serializers import StoreOrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = StoreOrder.objects.all()
    serializer_class = StoreOrderSerializer
