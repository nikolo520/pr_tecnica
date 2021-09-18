from django.db import models

# Create your models here.

class Rol(models.Model):
    nombre = models.CharField(null=True,blank=False,max_length=50)
    descripcion = models.TextField(null=True,max_length=100)
    
    def __str__(self) -> str:
        return self.nombre if self.nombre else 'NO definido'