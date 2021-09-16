from django.db import models

from apps.usuario.models import Usuario
from apps.cliente.models import Cliente
# Create your models here.
class Venta(models.Model):
    vendedor = models.ForeignKey(Usuario,null=True,blank=False,on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente,null=True,blank=False,on_delete=models.CASCADE)
    fecha = models.DateField()
    valor = models.CharField(max_length=50)
    servicio = models.CharField(max_length=50)