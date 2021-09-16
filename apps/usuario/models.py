from pr_tecnica.lists import *
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    nombres = models.CharField(null=True,blank=True,max_length=50)
    apellido1 = models.CharField(null=True,blank=True,max_length=50)
    apellido2 = models.CharField(null=True,blank=True,max_length=50)
    sexo = models.CharField(null=True,blank=True,max_length=50,choices=sexos_list)
    zona = models.CharField(null=True,blank=True,max_length=50,choices=zonas_list)
    departamento = models.CharField(null=True,blank=True,max_length=50)
    municipio = models.CharField(null=True,blank=True,max_length=50)
    jefe = models.ForeignKey('self', related_name="origin", null=True, blank=True, on_delete=models.CASCADE,default='')
    cargo = models.CharField(null=True,blank=True,max_length=50, choices=cargos_list,default='Ejecutivo_Comercial')
    correo = models.CharField(null=True,blank=True,max_length=50)
    telefono = models.CharField(null=True,blank=True,max_length=50)
    numero_empleado = models.CharField(null=True,blank=True,max_length=50)
    fecha_nacimiento = models.DateField(null=True,blank=True)
    fecha_ingreso = models.DateField(null=True,blank=True)
    identificacion = models.CharField(null=True,blank=True,max_length=50)
    foto = models.FileField(upload_to='uploads/',default='')
    activo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nombres + " " + self.apellido1 + " " + self.apellido2