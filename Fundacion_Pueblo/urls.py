from django import views
from django.contrib import admin
from django.urls import include, path 
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio, name='inicio'),

    #Aplicacion Usuario
    path('usuario/', include('Usuarios.urls')),
    path('usuario/', include('Usuarios.urls')),
    path('usuario/', include('Usuarios.urls')),
   

    #Aplicacion Eventos
    path('eventos/', include('Eventos.urls')),
    path('eventos/', include('Eventos.urls')),
    path('eventos/', include('Eventos.urls')),

]
