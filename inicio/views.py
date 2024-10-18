from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render
from inicio.forms import CrearPerroFormulario
from inicio.models import Perro


def inicio(request):
    return render(request,'index.html')

def buscar_perro(request):
    return render(request, 'buscar_perro.html',{'perro':''})

def crear_perro(request):
    
    formulario = CrearPerroFormulario()
    if request.method == 'POST':
        formulario = CrearPerroFormulario(request.POST)
        if formulario.isvalid():
            data = formulario.cleaned_data
            perro = Perro(nombre=data.get('nombre'),raza=data.get('raza'),edad=data.get('edad'))
            perro.save()
    return render(request,'crear_perro.html',{'form':formulario})
