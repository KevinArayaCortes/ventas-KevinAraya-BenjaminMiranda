from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Producto, Cliente, Pedido, Pedido_Producto
from .serializers import ProductoSerializer, ClienteSerializer, PedidoSerializer, PedidoProductoSerializer

# Vistas para Producto
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# Vistas para Cliente
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# Vistas para Pedido
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

# Vistas para Pedido_Producto
class Pedido_ProductoViewSet(viewsets.ModelViewSet):
    queryset = Pedido_Producto.objects.all()
    serializer_class = PedidoProductoSerializer