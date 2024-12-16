from django.contrib import admin
from django.urls import path, include
from appVenta import views  # Importa las vistas de la app appVenta
from Api import views as api_views  # Importa las vistas de la app Api

urlpatterns = [
    # Admin y vistas antiguas
    path('admin/', admin.site.urls),
    path('', views.index),
    path('productos', views.listadoProducto),
    path('agregarProducto', views.agregarProductos),
    path('actualizarProducto/<int:id>', views.actualizarProductos),
    path('eliminarProducto/<int:id>', views.eliminarProductos),
    path('princi/', views.Tabla),
    path('ag/', views.agClientes),
    path('actu/<int:id>', views.actualizarCli),
    path('borrar/<int:id>', views.borrarCli),
    path('pedido', views.listadoPedido),
    path('agregarPedido', views.agregarPedido),
    path('actualizarPedido/<int:id>', views.actualizarPedido),
    path('eliminarPedido/<int:id>', views.eliminarPedido),

    # Nuevas rutas de la API REST
    path('api/productos/', api_views.producto_list, name='producto-list'),
    path('api/productos/<int:pk>/', api_views.producto_detail, name='producto-detail'),
    path('api/clientes/', api_views.cliente_list, name='cliente-list'),
    path('api/clientes/<int:pk>/', api_views.cliente_detail, name='cliente-detail'),
    path('api/pedidos/', api_views.pedido_list, name='pedido-list'),
    path('api/pedidos/<int:pk>/', api_views.pedido_detail, name='pedido-detail'),
    path('api/pedidos-productos/', api_views.pedido_producto_list, name='pedido-producto-list'),
    path('api/pedidos-productos/<int:pk>/', api_views.pedido_producto_detail, name='pedido-producto-detail'),
]