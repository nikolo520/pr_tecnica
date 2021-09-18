from django import forms
from django.forms import widgets

from apps.usuario.models import User
from apps.rol.models import Rol
from apps.eps.models import Eps
class UsuarioForm(forms.Form):
    class Meta:
        model = User

        fields = [
            'documento',
            'nombres',
            'genero',
            'eps',
            'rol',
            'telefono',
            'fecha_nacimiento',
            'fecha_ingreso',

        ]

        labels = {
            'documento':'Documento',
            'nombres':'Nombre Completo',
            'genero':'Género',
            'eps':'Eps',
            'rol':'Rol',
            'telefono':'Teléfono',
            'fecha_nacimiento':'Fecha de Nacimiento',
            'fecha_ingreso':'Fecha de Ingreso',
        }

        widgets = {
            'documento': forms.TextInput(attrs={'class':'form-control'}),
            'nombres': forms.TextInput(attrs={'class':'form-control'}),
            'genero': forms.Select(attrs={'class':'form-control'}),
            'eps': forms.ModelChoiceField(queryset=Eps.objects.all(), to_field_name="eps"),
            'rol': forms.ModelChoiceField(queryset=Rol.objects.all(), to_field_name="rol"),
            'telefono': forms.Select(attrs={'class':'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_ingreso': forms.TextInput(attrs={'class':'form-control'}),
        }