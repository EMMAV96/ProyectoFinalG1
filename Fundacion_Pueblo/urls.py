
from django import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio, name='inicio'),
    path('cursos/', views.cursos, name='cursos'),
    path('iniciosesion/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('listaeventos/', views.index, name='listaeventos'),
]
