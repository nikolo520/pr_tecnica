from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from apps.usuario.forms import UsuarioForm
from apps.eps.models import Eps
#from apps.venta.models import Venta
from django.contrib.auth.decorators import login_required
# Create your views here.


# def login(request):

#     return render(request,'usuario/login.html')

@login_required
def index(request):
    epss = Eps.objects.all()
    contexto = {'epss' : epss}
    return render(request,'eps/index.html', contexto)

@login_required
def detail(request,id_eps):
    obj = Eps.objects.get(id=id_eps)
    contexto = {'eps':obj}
    return render(request,'eps/detail.html', contexto)


@login_required
def next(request,eps):
    obj = Eps.objects.get(eps=eps)
    return redirect('/eps/detail/' + str(obj.id))

@login_required
def create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('eps:index')
    else:
        form = UsuarioForm()
    return render(request,'eps/create.html',{'form':form})

@login_required
def edit(request):
    return render(request,'eps/detail.html')

@login_required
def delete(request):
    return render(request,'eps/detail.html')

# Create your views here.
