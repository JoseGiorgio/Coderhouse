from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Cuarto(models.Model):
    nombre = models.CharField(max_length=20)
    numero = models.IntegerField()
    capacidad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.numero} - {self.capacidad} personas"

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)   
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.edad} - {self.nacionalidad}"

class Empleado(models.Model):
    nombre = models.CharField(max_length=20)   
    apellido = models.CharField(max_length=20)
    puesto = models.CharField(max_length=30) 

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.puesto} "



class Avatar(models.Model):

    User = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", blank=True, null=True)