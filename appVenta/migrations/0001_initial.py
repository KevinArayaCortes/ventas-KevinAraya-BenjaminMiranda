# Generated by Django 3.2 on 2024-11-08 22:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text=' **El nombre no puede incluir espacios**', max_length=50, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator(regex='^[a-zA-Z]+$')])),
                ('apellido', models.CharField(help_text=' **El apellido no puede incluir espacios**', max_length=50, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator(regex='^[a-zA-Z]+$')])),
                ('rut', models.CharField(help_text=" (ej.'12345678-9')", max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\d{7,8}-[\\dkK]$')])),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.MinLengthValidator(2)])),
                ('direccion', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)])),
                ('telefono', models.CharField(help_text=" (ej.'912345678').", max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='El tipo solo debe contener letras (sin espacios ni números).', regex='^[A-Za-z]+$')])),
                ('Nombre', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='El nombre solo puede contener letras, números y espacios.', regex='^[A-Za-z0-9 ]+$')])),
                ('Descripcion', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='La descripción solo puede contener letras, números, comas, puntos y espacios.', regex='^[A-Za-z0-9,. ]+$')])),
                ('Stock', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='El stock no puede ser negativo.'), django.core.validators.MaxValueValidator(1000, message='El stock no puede superar las 1000 unidades.')])),
                ('Precio', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='El precio debe ser mayor que 0.')])),
            ],
        ),
    ]
