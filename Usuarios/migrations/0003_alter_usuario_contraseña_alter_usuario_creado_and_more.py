# Generated by Django 4.0 on 2021-12-14 04:52

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0002_alter_usuario_activo_alter_usuario_contraseña_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='contraseña',
            field=models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(8, message='La contraseña necesita ser mayor de 8 caracteres')]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='creado',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 12, 14, 4, 52, 31, 141808, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(3, message='El nombre de usuario debe tener mínimo 3 caracteres.'), django.core.validators.MaxLengthValidator(20, message='El nombre de usuario debe tener máximo 20 caracteres')]),
        ),
    ]
