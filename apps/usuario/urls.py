
from django.urls import path
from apps.usuario.views import index,detail,create,next
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', login_required(index),name='index'),
    path('detail/<id_usuario>/', login_required(detail),name='detail'),
    path('create/', login_required(create),name='create'),
]