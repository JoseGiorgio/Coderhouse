from django import forms
from .models import Empleado
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User



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

    

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )


    password1 = forms.CharField(label="contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="repetir contraseña",widget=forms.PasswordInput)

    class Meta:
        model=User       
        fields=["last_name", "first_name", "email"] 


    def clean_password2(self):

        print(self.cleaned_data)

        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2









