from django.contrib import admin
from .models import Producto, Pedido

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ['precio_total', 'created','updated']

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Pedido, PedidoAdmin)
