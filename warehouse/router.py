from rest_framework.routers import SimpleRouter
from .views import WarehouseOrderViewSet

warehouse_router = SimpleRouter()
warehouse_router.register(r'warehouse-orders', WarehouseOrderViewSet)
