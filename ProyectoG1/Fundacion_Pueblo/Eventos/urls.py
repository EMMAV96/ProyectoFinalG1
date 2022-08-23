from django.urls import path

from . import views


urlpatterns = [
    path('creareventos/', views.Crear.as_view())
]