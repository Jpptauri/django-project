from django.http import HttpResponse

def mi_vista(request):
    return HttpResponse('mi vista')

def inicio(request):
    return HttpResponse('inicio')

