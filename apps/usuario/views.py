from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from apps.usuario.forms import UsuarioForm
from apps.usuario.models import Usuario
from apps.venta.models import Venta
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):

    return render(request,'usuario/login.html')

@login_required
def index(request):
    usuarios = Usuario.objects.all()
    result = []
    for usuario in usuarios:
        temp = {
            'id' : usuario.id,
            'usuario' : usuario.usuario,
            'nombre_completo' : usuario.nombres + " " + usuario.apellido1 + " " + usuario.apellido2,
            'numero_empleado': usuario.numero_empleado,
            'cargo': usuario.cargo,
            'activo' : 'checked' if usuario.activo else ''

        }
        result.append(temp)
    contexto = {'usuarios' : result}
    return render(request,'usuario/index.html', contexto)

@login_required
def detail(request,id_usuario):
    obj = Usuario.objects.get(id=id_usuario)
    if obj.cargo == 'Ejecutivo_Comercial' or None:
        rel_objs = Venta.objects.filter(vendedor=obj)
        flag = False
    else:
        rel_objs = Usuario.objects.filter(jefe=obj)
        flag = True
    print(rel_objs)
    contexto = {'usuario':obj,'rel_objs':rel_objs,'flag':flag}
    return render(request,'usuario/detail.html', contexto)


@login_required
def next(request,usuario):
    obj = Usuario.objects.get(usuario=usuario)
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
