from django import forms

class  Cuartoformulario(forms.Form):

    nombre = forms.CharField()
    numero = forms.IntegerField()
    capacidad = forms.IntegerField()


class Clienteformulario(forms.Form):

    nombre = forms.CharField()   
    apellido = forms.CharField()
    edad = forms.IntegerField()
    nacionalidad = forms.CharField() 


class Empleadoformulario(forms.Form):
    nombre = forms.CharField()   
    apellido = forms.CharField()
    puesto = forms.CharField()     

