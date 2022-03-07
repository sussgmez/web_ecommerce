from django.contrib import admin
from .models import Product, Pedido

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ['precio_total', 'created','updated']

admin.site.register(Product, ProductAdmin)
admin.site.register(Pedido, PedidoAdmin)
