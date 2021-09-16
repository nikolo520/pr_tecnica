from django import forms
from django.forms import widgets

from apps.usuario.models import User

class UsuarioForm(forms.ModelForm):
    class Meta:
        modal = User

        fields = [
            'username',
            'usuario',
            'nombre',
            'zona',
            'ciudad',
            'jefe',
            'cargo',
            'email',
            'fecha_nacimiento',
            'fecha_ingreso',
            'identificacion',
        ]

        labels = {
            'username':'usuario',
            'usuario':'U',
            'nombre':'Nombre',
            'zona':'Zona',
            'ciudad':'Ciudad',
            'jefe':'Jefe',
            'cargo':'Cargo',
            'email':'Email',
            'fecha_nacimiento':'Fecha de Nacimiento',
            'fecha_ingreso':'Fecha de Ingreso',
            'identificacion':'Identificacion',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'usuario': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'zona': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad': forms.TextInput(attrs={'class':'form-control'}),
            'jefe': forms.Select(attrs={'class':'form-control'}),
            'cargo': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_ingreso': forms.TextInput(attrs={'class':'form-control'}),
            'identificacion': forms.TextInput(attrs={'class':'form-control'}),
        }