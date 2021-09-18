from django.db import models
from django.db.models.base import Model

# Create your models here.

class Eps(models.Model):
    nombre = models.CharField(null=True,blank=False,max_length=50)
    direccion = models.CharField(null=True,blank=True,max_length=50)
    telefono = models.CharField(null=True,blank=False,max_length=50)
    descripcion = models.TextField(null=True,max_length=100)

    def __str__(self) -> str:
        return self.nombre if self.nombre else 'NO definido'