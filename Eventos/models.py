from distutils.command.upload import upload
from email.mime import image
from turtle import update
from django.db import models

class Evento(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    fecha = models.CharField(max_length=200, verbose_name='Fecha de Inicio')
    descripcion = models.TextField(max_length=350, null=True, verbose_name='Descripcion')
    
    def __str__(self):
         eventos = "Nombre:" + self.nombre + "" + "Fecha de Inicio:" + self.fecha + "" + 'Descripcion:' + self.descripcion
         return eventos 
    
