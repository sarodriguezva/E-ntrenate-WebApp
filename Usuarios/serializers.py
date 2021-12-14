from django.db import models
from django.db.models import fields
from rest_framework import serializers
from Usuarios.models import Usuario

# Serializers help to convert the complex types of model instances into native python data types, that can be easy render into json or xml or other content types.

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields=('nombre', 'correo', 'contraseña', 'foto', 'rol', 'passwordChangeAt', 'passwordResetToken', 'passwordResetExpires', 'activo', 'creado')
        extra_kwargs = {'owner': {'read_only':True}}
        

