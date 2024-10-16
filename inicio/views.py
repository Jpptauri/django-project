from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render
from inicio.models import Auto

def mi_vista(request):
    return HttpResponse('mi vista')

def inicio(request):
    #return HttpResponse('<h1> inicio </h1>')
    return render(request,'index.html')
def vista_datos1(request,nombre):
    nombre_en_mayuscula = nombre.upper()
    return HttpResponse(f'hola {nombre_en_mayuscula}!!')

def primer_template(request):
    archivo = open(r'templates\primer_template.html')
    template = Template(archivo.read())
    contexto = Context()
    render_t = template.render(contexto)
    archivo.close()
    return(HttpResponse(render_t))

def segundo_template(request):
    fecha_actual = datetime.now()
    datos = {
        'fecha_actual':fecha_actual,
        'numeros':list(range(1,11))
    }
    
    #V1 
    #with open(r'templates\segundo_template.html') as archivo:
    #    template = Template(archivo.read())
    #contexto = Context(datos)
    #render_t = template.render(contexto)
    
    #V2
    #template = loader.get_template('segundo_template.html')
    #render_t = template.render(datos)
    #return(HttpResponse(render_t))
    
    #V3
    return render(request,'segundo_template.html',datos)

def crear_auto(request,marca,modelo,anio):
    auto = Auto(marca = marca,modelo = modelo,anio = anio)
    auto.save()
    return render(request,'crear_auto.html',{'auto':auto})
