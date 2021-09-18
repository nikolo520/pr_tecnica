from pr_tecnica.lists import *
from django.db import models
#from django.contrib.auth.models import AbstractUser
from apps.eps.models import Eps
from apps.rol.models import Rol


class User(models.Model):#AbstractUser):
    documento = models.CharField(null=True,blank=True,max_length=50)
    nombres = models.CharField(null=True,blank=True,max_length=50)
    genero = models.CharField(null=True,blank=True,max_length=50,choices=sexos_list)
    eps = models.ForeignKey(Eps, related_name="eps", null=True, blank=True, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, related_name="rol", null=True, blank=True, on_delete=models.CASCADE)
    telefono = models.CharField(null=True,blank=True,max_length=50)
    fecha_nacimiento = models.DateField(null=True,blank=True)
    fecha_creacion = models.DateTimeField(null=True,blank=True)
    

    def __str__(self) -> str:
        return self.nombres  if self.nombres else '' 
            
