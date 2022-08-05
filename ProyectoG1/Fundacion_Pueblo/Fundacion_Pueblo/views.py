from django.shortcuts import render 


def inicio(request):
    template_name = 'funciones/inicio.html'
    return render(request, template_name,{})

def cursos(request):
    template_name= 'funciones/cursos.html'
    return render(request, template_name,{})
