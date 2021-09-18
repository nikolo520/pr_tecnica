
from django.urls import path
from apps.rol.views import index,detail,create
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', login_required(index),name='index_rol'),
    path('detail/<id_rol>/', login_required(detail),name='detail_rol'),
    path('create/', login_required(create),name='create_rol'),
]