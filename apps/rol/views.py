from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from apps.usuario.forms import UsuarioForm
from apps.rol.models import Rol
#from apps.venta.models import Venta
from django.contrib.auth.decorators import login_required
# Create your views here.


# def login(request):

#     return render(request,'usuario/login.html')

@login_required
def index(request):
    rols = Rol.objects.all()
    contexto = {'rols' : rols}
    return render(request,'rol/index.html', contexto)

@login_required
def detail(request,id_rol):
    obj = Rol.objects.get(id=id_rol)
    contexto = {'rol':obj}
    return render(request,'rol/detail.html', contexto)


@login_required
def next(request,rol):
    obj = Rol.objects.get(rol=rol)
    return redirect('/rol/detail/' + str(obj.id))

@login_required
def create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('rol:index')
    else:
        form = UsuarioForm()
    return render(request,'rol/create.html',{'form':form})

@login_required
def edit(request):
    return render(request,'rol/detail.html')

@login_required
def delete(request):
    return render(request,'rol/detail.html')

# Create your views here.
