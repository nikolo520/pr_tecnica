from django.db import models

# Create your models here.
class Cliente(models.Model):
    fecha_ingreso = models.DateField()
    identificacion = models.CharField(null=True,blank=True,max_length=50)
    nombres = models.CharField(null=True,blank=True,max_length=50)
    apellidos = models.CharField(null=True,blank=True,max_length=50)
    ciudad = models.CharField(null=True,blank=True,max_length=50)
    email = models.EmailField()
    direccion = models.CharField(null=True,blank=True,max_length=50)
    telefono = models.CharField(null=True,blank=True,max_length=50)
