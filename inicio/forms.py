from django import forms

class CrearPerroFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    raza = forms.CharField(max_length=20)
    edad = forms.IntegerField()