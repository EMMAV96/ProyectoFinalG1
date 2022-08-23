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

def cursos(request):
    template_name= 'funciones/cursos.html'
    return render(request, template_name,{})

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


def index(request):
    template_name = 'eventos/index.html'
    eventos = Evento.objects.all()
    ctx = {
        'eventos': eventos
    }
    return render (request, template_name, ctx)
""""
def crear(request):
    template_name = 'eventos/crear.html'
    formulario = EventoForm(request.POST, request.FILES )
    if formulario.is_valid():
        formulario.save()
        return redirect('listaeventos')
    ctx = {
        'formulario': formulario
    }
    return render(request, template_name, ctx)


def eliminar(request, id):
    evento = Evento.objects.get(id=id)
    evento.delete()
    return redirect('listaeventos')"""