from rest_framework.routers import SimpleRouter

from store.views import OrderViewSet

store_router = SimpleRouter()
store_router.register(r'store-orders', OrderViewSet)
