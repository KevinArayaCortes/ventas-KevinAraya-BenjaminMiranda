from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator, MinLengthValidator

# Modelo de Producto
class Producto(models.Model):
    Tipo = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex='^[A-Za-z]+$',
                message='El tipo solo debe contener letras (sin espacios ni números).'
            )
        ]
    )
    Nombre = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex='^[A-Za-z0-9 ]+$',
                message='El nombre solo puede contener letras, números y espacios.'
            )
        ]
    )
    Descripcion = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex='^[A-Za-z0-9,. ]+$',
                message='La descripción solo puede contener letras, números, comas, puntos y espacios.'
            )
        ]
    )
    Stock = models.IntegerField(
        validators=[
            MinValueValidator(0, message='El stock no puede ser negativo.'),
            MaxValueValidator(1000, message='El stock no puede superar las 1000 unidades.')
        ]
    )
    Precio = models.IntegerField(
        validators=[
            MinValueValidator(1, message='El precio debe ser mayor que 0.')
        ]
    )

    def __str__(self):
        return f"{self.id} - {self.Nombre}"

# Modelo de Cliente
class Cliente(models.Model):
    nombre = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2), RegexValidator(regex=r'^[a-zA-Z]+$')],
        help_text=" **El nombre no puede incluir espacios**"
    )
    apellido = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2), RegexValidator(regex=r'^[a-zA-Z]+$')],
        help_text=" **El apellido no puede incluir espacios**"
    )
    rut = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^\d{7,8}-[\dkK]$')],
        help_text=" (ej.'12345678-9')"
    )
    email = models.EmailField(
        validators=[MinLengthValidator(2)]
    )
    direccion = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)]
    )
    telefono = models.CharField(
        max_length=9,
        validators=[RegexValidator(regex=r'^\d{9}$', message="El teléfono debe contener 9 dígitos.")],
        help_text=" (ej.'912345678')."
    )

    def __str__(self):
        return f"{self.id} - {self.nombre}"

# Modelo de Pedido
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    cantidad_productos = models.IntegerField(
        validators=[MinValueValidator(1, message='La cantidad debe ser al menos 1.')]
    )
    descripcion = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(5)]
    )
    estado = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(3)]
    )

# Modelo de Pedido_Producto
class Pedido_Producto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
