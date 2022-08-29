from django.contrib.auth.views import LoginView
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name ='user'

urlpatterns = [
    path('iniciosesion/', views.Login.as_view(), name= 'login'),
    path('registro/', views.registro, name= 'registro'),
    path('cerrarsesion/', views.logout, name='logout'),
   
]