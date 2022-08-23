from audioop import reverse
from venv import create
from django.shortcuts import render
from django.views.generic.edit import CreateView

from .forms import EventoForm
from .models import Evento


class Crear(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/crear.html'

    def get_success_url(self):
        return reverse('inicio')