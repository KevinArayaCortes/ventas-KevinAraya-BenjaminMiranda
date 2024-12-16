from django.contrib import admin
from Api.models import Producto, Cliente, Pedido

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['Tipo', 'Nombre', 'Descripcion', 'Stock', 'Precio']

admin.site.register(Producto, ProductoAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display= ['nombre', 'apellido' ,'rut', 'email' ,'direccion', 'telefono']

admin.site.register(Cliente, ClienteAdmin)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'fecha', 'cantidad_productos', 'descripcion', 'estado']

admin.site.register(Pedido, PedidoAdmin)