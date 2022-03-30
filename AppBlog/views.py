from msilib import datasizemask
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, usuarios, Infoususario
from django.utils import timezone
from AppBlog.forms import CrearblogFormulario, CrearblogUsuario,CrearInfoususario
from django.views.generic import ListView, DetailView

# Create your views here.

def inicio(request):
    return render(request, 'AppBlog/index.html')

def crearblog(request):
    if request.method =="POST":
        crear = CrearblogFormulario(request.POST)
        if crear.is_valid():
         data = crear.cleaned_data
         blog_nuevo = Post(data['titulo'], data['autor'], data['texto'] )
         blog_nuevo.save()
        return render(request, 'AppBlog/index.html')
    else:
        crear = CrearblogFormulario()

    return render(request, 'AppBlog/crearblog.html', {"formulario": crear})

def buscar(request):

    data = request.GET.get('titulo', "")
    error = ""

    if data:
        try:
            post =  Post.objects.get(titulo=data)
            return render(request, 'AppBlog/buscar_titulo.html', {"post": post, "id": data})

        except Exception as exc:
            print(exc)
            error = "No existe ese titulo post"
    return render(request, 'AppBlog/buscar_titulo.html', {"error": error})


def usuario(request):
    if request.method =="POST":
        crear = CrearblogUsuario(request.POST)
        if crear.is_valid():
         data = crear.cleaned_data
         usuario_nuevo = usuarios(data['nombre'], data['apellido'], data['email'] )
         usuario_nuevo.save()
        return render(request, 'AppBlog/index.html')
    else:
        crear = CrearblogUsuario()

    return render(request, 'AppBlog/crearusuario.html', {"formulario": crear})
def infoususario(request):
    if request.method =="POST":
        crear = CrearInfoususario(request.POST)
        if crear.is_valid():
         data = crear.cleaned_data
         info_usuario_nuevo = Infoususario(data['color_favorito'], data['genero'], data['equipo_favorito'] )
         info_usuario_nuevo.save()
        return render(request, 'AppBlog/index.html')
    else:
        crear = CrearInfoususario()

    return render(request, 'AppBlog/infousuario.html', {"formulario": crear})


def borrarblog(request):
    return render(request, 'AppBlog/borrar.html')

def contacto(request):
    return render(request, 'AppBlog/contacto.html')