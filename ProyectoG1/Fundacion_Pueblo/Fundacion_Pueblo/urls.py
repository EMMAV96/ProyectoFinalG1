
from django import views
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio, name='inicio'),
    path('cursos/', views.cursos, name='cursos'),
]
