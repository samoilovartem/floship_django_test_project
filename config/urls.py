from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from store.router import store_router
from warehouse.router import warehouse_router

main_router = routers.DefaultRouter()
main_router.registry.extend(store_router.registry)
main_router.registry.extend(warehouse_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(main_router.urls)),
]
