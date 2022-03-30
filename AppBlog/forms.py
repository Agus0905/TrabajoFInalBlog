from email.policy import default
from django import forms
from django.utils import timezone

class CrearblogFormulario(forms.Form):
    titulo = forms.CharField(max_length=100)
    autor = forms.CharField(max_length=50)
    texto = forms.CharField(widget = forms.Textarea)
    categoria = forms.CharField(max_length=30)
    fecha_creacion = forms.DateField(initial=timezone.now)

class CrearblogUsuario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    edad = forms.IntegerField()

class CrearInfoususario(forms.Form):
    color_favorito = forms.CharField(max_length=50)
    genero =  forms.CharField(max_length=50)
    equipo_favorito = forms.CharField(max_length=50)
