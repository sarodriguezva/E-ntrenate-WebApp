# Generated by Django 4.0 on 2021-12-14 02:45

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(3, 'El nombre de usuario debe tener mínimo 3 caracteres.'), django.core.validators.MaxLengthValidator(20, 'El nombre de usuario debe tener máximo 20 caracteres')])),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('contraseña', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(8, 'La contraseñanecesita ser mayor de 8 caracteres')])),
                ('foto', models.CharField(default='default.jpg', max_length=500)),
                ('rol', models.CharField(choices=[('es', 'Estudiante'), ('pr', 'Profesor')], default='es', max_length=20)),
                ('passwordChangeAt', models.DateField()),
                ('passwordResetToken', models.CharField(max_length=100)),
                ('passwordResetExpires', models.DateField()),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateField(default=datetime.datetime(2021, 12, 14, 2, 44, 50, 104904, tzinfo=utc))),
            ],
        ),
    ]