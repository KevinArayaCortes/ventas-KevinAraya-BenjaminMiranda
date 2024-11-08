from django.contrib import admin
from appVenta.models import Producto, Cliente

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['Tipo', 'Nombre', 'Descripcion', 'Stock', 'Precio']

admin.site.register(Producto, ProductoAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display= ['nombre', 'apellido' ,'rut', 'email' ,'direccion', 'telefono']

admin.site.register(Cliente, ClienteAdmin)