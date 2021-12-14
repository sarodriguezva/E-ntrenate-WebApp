from django import forms
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils import timezone


# Create your models here.
# Deberia poner los schemas aca?

class Curso(models.Model):
    nombre = models.CharField(unique=True, blank=False, max_length=20,
    validators=[
        MinLengthValidator(3, message='El curso debe tener mínimo 3 caracteres.'), 
        MaxLengthValidator(20, message='El curso debe tener máximo 20 caracteres')])
    imagen = models.CharField(max_length=500, default='default.jpg', blank=True)
    activo = models.BooleanField(default=True, blank=True)
    creado = models.DateField(default= timezone.now, blank=True)
    secciones = models.JSONField(encoder=object, default=dict) # No pued pasarle un mutable es decir [] o {} ya que si hago por ejemplo realizo un update en uno de estos fields que tienen por defecto el mutable me los cambiaria todos.





