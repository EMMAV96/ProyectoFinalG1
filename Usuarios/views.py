from xml.etree.ElementTree import register_namespace
from django.contrib import messages
from re import template
from django.shortcuts import render, redirect 
from Usuarios.forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from Eventos.models import Evento
from django.contrib.auth.mixins import LoginRequiredMixin
from Eventos.forms import EventoForm


class Login(LoginView, LoginRequiredMixin):
    template_name= 'paginas/iniciosesion.html'

def logout(request):
    return redirect('user:login')

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
        
            return redirect('user:login')
    else:
        form= UserRegisterForm()
    
    ctx =  {
        'form' : form
    }
    template_name= 'paginas/registro.html'
    return render(request, template_name,ctx)

