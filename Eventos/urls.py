
from django.urls import path

from . import views

app_name ='eventos'

urlpatterns = [
    path('creareventos/', views.Crear.as_view(), name= 'crear'),
    path('lista/', views.Lista.as_view(), name= 'lista'),
    path('modificar/<int:pk>', views.Modificar.as_view(), name= 'modificar'),
    path('eliminar/<int:pk>', views.Eliminar.as_view(), name= 'eliminar'),
]