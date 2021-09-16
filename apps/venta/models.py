from django.db import models

from apps.usuario.models import User
from apps.cliente.models import Cliente
# Create your models here.
class Venta(models.Model):
    vendedor = models.ForeignKey(User,null=True,blank=False,on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente,null=True,blank=False,on_delete=models.CASCADE)
    fecha = models.DateField()
    valor = models.DecimalField(max_length=50,decimal_places=2,max_digits=15)
    servicio = models.CharField(max_length=50)