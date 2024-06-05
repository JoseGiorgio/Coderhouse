from django.shortcuts import render
from appHostel.models import Cuarto, Cliente, Empleado
from .forms import Cuartoformulario, Clienteformulario, Empleadoformulario 

# Views .

def agregar_cuarto(req):

    if  req.method == "POST":

        miFormulario = Cuartoformulario(req.POST)

        if miFormulario.is_valid():

            informacion =  miFormulario.cleaned_data

            cuarto  = Cuarto(nombre = informacion["nombre"], numero = informacion["numero"], capacidad = informacion["capacidad"]) 
            cuarto.save()

            return render(req, "inicio.html", {"mensaje": "Los datos se cargan correctamente"}) 
        else:
            return render(req, "inicio.html", {"mensaje": "Los datos son invalidos"}) 

    else:
        miFormulario = Cuartoformulario()

        return render(req, "cuartoFormulario.html", {"miFormulario": miFormulario})


   

def agregar_cliente(req):

    if  req.method == "POST":

        miFormulario = Clienteformulario(req.POST)

        if miFormulario.is_valid():

            informacion =  miFormulario.cleaned_data

            cliente = Cliente(nombre = informacion["nombre"], apellido = informacion["apellido"], edad = informacion["edad"], nacionalidad = informacion["nacionalidad"]) 
            cliente.save()

            return render(req, "inicio.html", {"mensaje": "Los datos se cargan correctamente"}) 
        else:
            return render(req, "inicio.html", {"mensaje": "Los datos son invalidos"}) 
    else:
        miFormulario = Clienteformulario()

        return render(req, "clienteFormulario.html", {"miFormulario": miFormulario})    
    



def agregar_empleado(req):
    
    if  req.method == "POST":

        miFormulario = Empleadoformulario(req.POST)

        if miFormulario.is_valid():

            informacion =  miFormulario.cleaned_data

            empleado = Empleado(nombre = informacion["nombre"], apellido = informacion["apellido"], puesto = informacion["puesto"]) 
            empleado.save()

            return render(req, "inicio.html", {"mensaje": "Los datos se cargan correctamente"}) 
        else:
            return render(req, "inicio.html", {"mensaje": "Los datos son invalidos"}) 
    else:
        miFormulario = Empleadoformulario()

        return render(req, "empleadoFormulario.html", {"miFormulario": miFormulario})  










def inicio(req):

    return render(req, "inicio.html" ,{})    

def cuartos(req):

    return render(req, "cuarto.html" ,{})    

def clientes(req):

    return render(req, "cliente.html" ,{})    

def empleados(req):

    return render(req, "empleado.html" ,{})    



def lista_empleado(req):

    mis_empleados = Empleado.objects.all()

    return render(req, "listaEmpleado.html", {"empleados": mis_empleados})  




def buscar_puesto(req):
    return render(req, "buscarpuesto.html", {})

def buscar(req):
    if "nombre" in req.GET and req.GET["nombre"]:
        nombre = req.GET["nombre"]
        empleados = Empleado.objects.filter(nombre__icontains=nombre)

        if empleados.exists():
            return render(req, "resultadoBusqueda.html", {"empleados": empleados, "nombre": nombre})
        else:
            return render(req, "inicio.html", {"mensaje": "No se encontraron empleados con ese nombre"})
    else:
        return render(req, "inicio.html", {"mensaje": "Los datos no son correctos"})


