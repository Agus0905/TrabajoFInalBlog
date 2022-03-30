from django.urls import path
from .views import *
urlpatterns = [
    path('', inicio, name='inicio'),
    path('crearblog/', crearblog, name='Crearblog'),
   path('buscar_titulo/', buscar, name='buscartitulo'),
    path('borrar_blog/', borrarblog, name='borrarblog'),
    path('contacto/', contacto, name='contacto'),
    path('crearusuario/', usuario, name='usuario'),
    path('infousuario/', infoususario, name='info_usuario'),

]