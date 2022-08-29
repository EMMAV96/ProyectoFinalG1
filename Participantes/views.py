from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView

from Participantes.models import Estudiantes

class CrearLugar(CreateView):
    model = Estudiantes
    template_name = 'participantes/inscribirse.html'

    def get_success_url(self, **kwargs):
        return reverse('inicio', args=[])
