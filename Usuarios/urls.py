from django.contrib.auth.views import LoginView, logout_then_login
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name ='usuarios'

urlpatterns = [
    path('iniciosesion/', views.Login.as_view(), name= 'login'),
    path('registro/', views.registro, name= 'registro'),
    path('cerrarsesion/', auth_views.logout_then_login, name= 'logout'),
   
]