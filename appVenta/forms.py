from django import forms
from appVenta.models import Producto, Cliente

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'