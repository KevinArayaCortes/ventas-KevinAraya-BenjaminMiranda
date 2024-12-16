from rest_framework import serializers
from .models import Producto, Cliente, Pedido, Pedido_Producto

# Serializador para Producto
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'  # Incluye todos los campos del modelo
        # Si necesitas excluir algún campo, usa: fields = ['campo1', 'campo2']

# Serializador para Cliente
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

# Serializador para Pedido
class PedidoSerializer(serializers.ModelSerializer):
    cliente = serializers.StringRelatedField()  # Representa el cliente como su método __str__
    
    class Meta:
        model = Pedido
        fields = '__all__'

# Serializador para Pedido_Producto
class PedidoProductoSerializer(serializers.ModelSerializer):
    pedido = serializers.StringRelatedField()  # Representa el pedido como su método __str__
    producto = serializers.StringRelatedField()  # Representa el producto como su método __str__

    class Meta:
        model = Pedido_Producto
        fields = '__all__'
