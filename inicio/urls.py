from django.urls import path
from inicio.views import inicio,crear_perro,buscar_perro

urlpatterns = [
    path('', inicio),
    path('buscar-perro/', buscar_perro),
    path('crear-perro/',crear_perro)
]