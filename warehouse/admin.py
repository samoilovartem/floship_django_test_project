from django.contrib import admin

from warehouse.models import WarehouseOrder


class WarehouseOrderAdminConfig(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'quantity', 'status')
    fields = ('id', 'product_name', 'quantity', 'status', 'sync')
    readonly_fields = ('id',)


admin.site.register(WarehouseOrder, WarehouseOrderAdminConfig)
