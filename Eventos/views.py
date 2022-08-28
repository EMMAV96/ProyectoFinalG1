from django.urls import reverse
from venv import create
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import EventoForm
from .models import Evento


class Crear(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/crear.html'

    def get_success_url(self, **kwargs):
        return reverse('eventos:lista', args=[])

class Lista(ListView):
    template_name='eventos/listaeventos.html'
    model=Evento
    context_object_name = 'eventos'

class Modificar(UpdateView):
    template_name='eventos/editar.html'
    model=Evento
    form_class = EventoForm
    context_content_name = 'eventos'

    def get_success_url(self, **kwargs):
        return reverse('eventos:lista')

class Eliminar(DeleteView):
    template_name='eventos/eliminar.html'
    model=Evento

    def get_success_url(self, **kwargs):
        return reverse('eventos:lista', args=[])
    
