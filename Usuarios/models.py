from django import forms
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils import timezone


# Create your models here.
# Deberia poner los schemas aca?

class Usuario(models.Model):
    ROL_CHOICES = [('es', 'Estudiante'), ('pr', 'Profesor')]
    nombre = models.CharField(unique=True, blank=False, max_length=20,
    validators=[
        MinLengthValidator(3, message='El nombre de usuario debe tener mínimo 3 caracteres.'), 
        MaxLengthValidator(20, message='El nombre de usuario debe tener máximo 20 caracteres')])
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=40,
        validators=[MinLengthValidator(8, message='La contraseña necesita ser mayor de 8 caracteres')])
    # confirmarContraseña = models.CharField(validators=[<Crar mi validación>])
    foto = models.CharField(max_length=500, default='default.jpg', blank=True)
    rol = models.CharField(default='es', choices=ROL_CHOICES, max_length=20, blank=True)
    passwordChangeAt = models.DateField(blank=True)
    passwordResetToken = models.CharField(max_length=100, blank=True)
    passwordResetExpires = models.DateField(blank=True)
    activo = models.BooleanField(default=True, blank=True)
    creado = models.DateField(default= timezone.now, blank=True) # Para estos tengo que crear el schema porque nunca se van a encontrar en el formulario, se crean pr defecto pero desde aqui no puedo meterlos a Mongo.

    # def isExist(self):
    #     return Usuario.objects.filter(correo = self.correo)
            





