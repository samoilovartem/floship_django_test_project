from rest_framework import viewsets
from .models import WarehouseOrder
from .serializers import WarehouseOrderSerializer


class WarehouseOrderViewSet(viewsets.ModelViewSet):
    queryset = WarehouseOrder.objects.all()
    serializer_class = WarehouseOrderSerializer


# @csrf_exempt
# def receive_order(request):
#     if request.method == 'POST':
#         data = request.POST
#         order = StoreOrder(
#             product_name=data.get('product_name'),
#             quantity=data.get('quantity'),
#             status=data.get('status'),
#         )
#         order.save()
#         return JsonResponse({'message': 'Order received'}, status=status.HTTP_201_CREATED)
#     else:
#         return JsonResponse({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)
