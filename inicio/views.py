from django.http import HttpResponse

def mi_vista(request):
    return HttpResponse('mi vista')

def inicio(request):
    return HttpResponse('<h1> inicio </h1>')

def vista_datos1(request,nombre):
    nombre_en_mayuscula = nombre.upper()
    return HttpResponse(f'hola {nombre_en_mayuscula}!!')
