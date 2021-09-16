
from django.urls import path
from apps.cliente.views import index

app_name = 'cliente'

urlpatterns = [
    path('', index,name='index'),
]