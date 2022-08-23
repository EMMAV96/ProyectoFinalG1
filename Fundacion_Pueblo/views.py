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

def login(request):
    template_name= 'paginas/iniciosesion.html'
    return render(request, template_name,{})

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            """"
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado',extra_tags="", fail_silently=False)
            """
            return redirect('login')
    else:
        form= UserRegisterForm()
    
    ctx =  {
        'form' : form
    }
    template_name= 'paginas/registro.html'
    return render(request, template_name,ctx)

