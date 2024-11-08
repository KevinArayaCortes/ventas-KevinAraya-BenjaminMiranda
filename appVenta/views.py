from django.shortcuts import render, redirect
from appVenta.forms import ProductoForm, FormCliente
from appVenta.models import Producto, Cliente

def index(request):
    return render(request, 'appVenta/index.html')

def listadoProducto(request):
    productos = Producto.objects.all()
    data = {'productos': productos}
    return render(request, 'appVenta/productos.html', data)

def agregarProductos(request):
    form = ProductoForm()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/productos')
        else:
            return render(request, 'appVenta/agregarProducto.html', {'form': form})
    data = {'form': form}
    return render(request, 'appVenta/agregarProducto.html', data)

def actualizarProductos(request, id):
    producto = Producto.objects.get(id=id)
    form = ProductoForm(instance=producto)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('/productos')
    data = {'form': form}
    return render(request, 'appVenta/agregarProducto.html', data)

def eliminarProductos(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('/productos')

def Tabla(request):
    cliente = Cliente.objects.all()
    data = {'cliente': cliente}
    return render(request, 'appVenta/tabla.html', data)

def agClientes(request):
    form = FormCliente()
    if request.method == 'POST':
        form = FormCliente(request.POST)
        if form.is_valid():
            form.save()
    data = {'form': form}
    return render(request, 'appVenta/agCliente.html', data)

def actualizarCli(request, id):
    cliente =  Cliente.objects.get(id = id)
    form = FormCliente(instance= cliente)
    if request.method == 'POST':
        form = FormCliente(request.POST, instance= cliente)
        if form.is_valid():
            form.save()
        return Tabla(request)
    data = {'form': form}
    return render(request, 'appVenta/agCliente.html', data)

def borrarCli(request, id):
    cliente =  Cliente.objects.get(id = id)
    cliente.delete()
    return redirect('/princi')