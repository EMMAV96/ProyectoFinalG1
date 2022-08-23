
from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control" }))
    fecha = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control" }))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control mb-3"}))
    class Meta:
        model = Evento
        fields = '__all__'

    
        