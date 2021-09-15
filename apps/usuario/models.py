from pr_tecnica.lists import *
from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(null=True,blank=True,max_length=50)
    nombres = models.CharField(null=True,blank=True,max_length=50)
    apellido1 = models.CharField(null=True,blank=True,max_length=50)
    apellido2 = models.CharField(null=True,blank=True,max_length=50)
    sexo = models.CharField(null=True,blank=True,max_length=50,choices=sexos_list)
    zona = models.CharField(null=True,blank=True,max_length=50,choices=zonas_list)
    departamento = models.CharField(null=True,blank=True,max_length=50)
    municipio = models.CharField(null=True,blank=True,max_length=50)
    jefe = models.ForeignKey('self', related_name="origin", null=True, blank=True, on_delete=models.CASCADE,default='')
    cargo = models.CharField(null=True,blank=True,max_length=50, choices=cargos_list)
    email = models.CharField(null=True,blank=True,max_length=50)
    telefono = models.CharField(null=True,blank=True,max_length=50)
    numero_empleado = models.CharField(null=True,blank=True,max_length=50)
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()
    identificacion = models.CharField(null=True,blank=True,max_length=50)
    activo = models.BooleanField(default=True)