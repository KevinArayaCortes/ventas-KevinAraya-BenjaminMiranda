from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Api import views as api_views
from appVenta import views

# Configuración del router
router = DefaultRouter()
router.register(r'productos', api_views.ProductoViewSet, basename='producto')
router.register(r'clientes', api_views.ClienteViewSet, basename='cliente')
router.register(r'pedidos', api_views.PedidoViewSet, basename='pedido')
router.register(r'pedidos-productos', api_views.Pedido_ProductoViewSet, basename='pedido-producto')

urlpatterns = [
    # Admin y vistas antiguas
    path('admin/', admin.site.urls),
    path('a', views.index),
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

    # Nuevas rutas de la API REST usando el router
    path('', include(router.urls)),  # Incluye las rutas generadas por el router
]
