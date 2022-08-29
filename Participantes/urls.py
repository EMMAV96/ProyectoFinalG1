
from django.urls import path

from . import views

app_name ='participantes'

urlpatterns = [
    path('crearlugar/<int:pk>', views.CrearLugar.as_view(), name= 'lugar'),
]