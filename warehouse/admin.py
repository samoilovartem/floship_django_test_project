from django.contrib import admin

from .models import WarehouseOrder


class WarehouseOrderAdminConfig(admin.ModelAdmin):
    list_display = (
        'id',
        'product_name',
        'quantity',
        'status'
    )
    fields = (
        'id',
        'product_name',
        'quantity',
        'status'
    )
    readonly_fields = ('id',)


admin.site.register(WarehouseOrder, WarehouseOrderAdminConfig)
