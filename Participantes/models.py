from django.db import models
from Eventos.models import Evento
from Usuarios.forms import User

class Estudiantes(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='eventos')
    participantes= models.ManyToManyField(User)

    class Meta:
        db_table = 'inscriptos'