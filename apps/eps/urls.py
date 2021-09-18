
from django.urls import path
from apps.eps.views import index,detail,create
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', login_required(index),name='index_eps'),
    path('detail/<id_eps>/', login_required(detail),name='detail_eps'),
    path('create/', login_required(create),name='create_eps'),
]