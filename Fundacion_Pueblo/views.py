from email import message
from django.contrib import messages
from pyexpat.errors import messages 
from re import template
from django.shortcuts import render, redirect 
from Usuarios.forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from Eventos.models import Evento
from Eventos.forms import EventoForm



def inicio(request):
    template_name = 'paginas/inicio.html'
    eventos = Evento.objects.filter()
    ctx = {
        'eventos': eventos
    }
    return render(request, template_name,ctx)
    
