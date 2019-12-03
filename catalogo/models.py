from django.db import models
from django.urls import reverse
# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=16)
    email = models.EmailField(max_length=100)
    fecha = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre
