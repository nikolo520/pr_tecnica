from django.urls import  path
from apps.venta.views import index

app_name = 'venta'

urlpatterns = [
    path('', index,name='index'),
]