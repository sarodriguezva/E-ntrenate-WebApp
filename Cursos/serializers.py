from django.db.models import fields
from rest_framework import serializers
from Cursos.models import Curso

# Serializers help to convert the complex types of model instances into native python data types, that can be easy render into json or xml or other content types.

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Curso
        fields=('nombre', 'imagen', 'activo', 'creado', 'secciones')
        

