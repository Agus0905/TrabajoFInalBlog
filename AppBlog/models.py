
from django.conf import settings
from django.db import models
from django.forms import IntegerField
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=100, primary_key=True)
    autor = models.CharField(max_length=60)
    texto = models.TextField(help_text="Ingrese el contenido de su blog")
    categoria = models.CharField(max_length=30)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)

class usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50,primary_key=True)
    email = models.EmailField()
    edad = models.IntegerField(default=True)

class Infoususario(models.Model):
    color_favorito = models.CharField(max_length=50)
    genero =  models.CharField(max_length=50,primary_key=True)
    equipo_favorito = models.CharField(max_length=50)