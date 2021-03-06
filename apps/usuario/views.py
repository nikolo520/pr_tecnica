from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from apps.usuario.forms import UsuarioForm
from apps.usuario.models import User
#from apps.venta.models import Venta
from django.contrib.auth.decorators import login_required
# Create your views here.


# def login(request):

#     return render(request,'usuario/login.html')

@login_required
def index(request):
    usuarios = User.objects.all()
    result = []
    contexto = {'usuarios' : usuarios}
    return render(request,'usuario/index.html', contexto)

@login_required
def detail(request,id_usuario):
    obj = User.objects.get(id=id_usuario)
    contexto = {'usuario':obj}
    return render(request,'usuario/detail.html', contexto)


@login_required
def next(request,usuario):
    obj = User.objects.get(usuario=usuario)
    return redirect('/usuario/detail/' + str(obj.id))

@login_required
def create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('usuario:index')
    else:
        form = UsuarioForm()
    return render(request,'usuario/create.html',{'form':form})

@login_required
def edit(request):
    return render(request,'usuario/detail.html')

@login_required
def delete(request):
    return render(request,'usuario/detail.html')

# Create your views here.
