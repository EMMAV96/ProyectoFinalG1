
from django import views
from django.contrib import admin
from django.urls import include, path 
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio, name='inicio'),
    path('iniciosesion/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
   
    #Aplicacion Eventos
    path('eventos/', include('Eventos.urls'), name='creareventos'),
]
