from django.contrib import admin

from store.models import StoreOrder


class StoreOrderAdminConfig(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'quantity', 'status')
    fields = ('id', 'product_name', 'quantity', 'status', 'sync')
    readonly_fields = ('id',)


admin.site.register(StoreOrder, StoreOrderAdminConfig)
