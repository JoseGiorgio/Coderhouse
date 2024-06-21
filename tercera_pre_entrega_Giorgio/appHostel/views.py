from django.shortcuts import render
from appHostel.models import Cuarto, Cliente, Empleado, Avatar
from .forms import Cuartoformulario, Clienteformulario,Empleadoformulario, UserEditForm, AvatarFormulario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# Views .
@staff_member_required(login_url="/appHostel/login")
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


   
@staff_member_required(login_url="/appHostel/login")
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
    


@staff_member_required(login_url="/appHostel/login")
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
    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, "inicio.html", {"url": avatar.imagen.url})
    except:
        return render(req, "inicio.html")    

def cuartos(req):

    return render(req, "cuarto.html" ,{})    

def clientes(req):

    return render(req, "cliente.html" ,{})    

def empleados(req):

    return render(req, "empleado.html" ,{})    

@staff_member_required(login_url="/appHostel/login")
def lista_empleado(req):

    mis_empleados = Empleado.objects.all()

    return render(req, "listaEmpleado.html", {"empleados": mis_empleados})  



@staff_member_required(login_url="/appHostel/login")
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


def empleadoEditado(req,id): 

    if req.method == "POST":

        miFormulario = Empleadoformulario(req.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            empleado = Empleado.objects.get(id = id)

            empleado.nombre = informacion["nombre"]
            empleado.apellido = informacion["apellido"]
            empleado.puesto = informacion["puesto"]
           
            empleado.save()

            return render (req,"inicio.html",{"mensaje":"Empleado actualizado con exito"})
        else:
            return render (req,"inicio.html",{"mensaje":"Datos invalidos"})

    else:
        empleado = Empleado.objects.get(id = id)

        miFormulario = Empleadoformulario(initial={
          "nombre": empleado.nombre,
          "apellido": empleado.apellido,
          "puesto": empleado.puesto,  
        })

        return render(req,"editarEmpleado.html",{"miFormulario": miFormulario, "id":  empleado.id})
    

def eliminarEmpleado(req,id):

    if req.method == 'POST':


        empleado = Empleado.objects.get(id=id)
        empleado.delete()

        mis_empleados = Empleado.objects.all()

    return render(req,"listaEmpleado.html",{"empleados": mis_empleados})




def about(req):
    return render(req,"about.html")




def login_view(req):
        
    if req.method == "POST":    

        miFormulario = AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario = informacion["username"]
            pss = informacion["password"]

            user = authenticate(username = usuario, password =pss)

            if user:
                login(req, user)
                return render (req,"inicio.html",{"mensaje":f"Ha ingresado a la sesion de {usuario}"})
            else:
                return render (req, "inicio.html", {"mensaje":"Los datos no son correctos"})
        
        else:
            return render (req, "inicio.html", {"mensaje":"Los datos no son validos"})

    else:
        miFormulario = AuthenticationForm()

        return render(req, "login.html", {"miFormulario": miFormulario})    



def register(req):
    if req.method == "POST":
        
        miFormulario = UserCreationForm(req.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            usuario = informacion["username"]
            miFormulario.save()

            return render(req, "inicio.html", {"mensaje":f"Usuario {usuario} creado correctamente!!"})
        
        else:
            return render(req, "inicio.html", {"mensaje":"Los datos no son validos"})
        
    else:
        miFormulario = UserCreationForm()
        return render(req, "registrar.html", {"miFormulario": miFormulario}) 


@login_required
def editar_perfil(req):

    usuario = req.user

    if req.method == "POST":
        miFormulario = UserEditForm(req.POST, instance =req.user)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.email = informacion["email"]
            usuario.set_password(informacion["password1"])

            usuario.save()

            return render(req,"inicio.html",{"mensaje":"Los datos se actualizaron con exito!"})
        else:
            return render(req,"inicio.html", {"mensaje": "Los datos no son correctos"})

    else:

        miFormulario = UserEditForm(instance = req.user)
        return render(req,"editarPerfil.html",{"miFormulario": miFormulario})
    


def agregar_avatar(req):

    if req.method == "POST":

        miFormulario = AvatarFormulario(req.POST, req.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            
            avatar = Avatar(user=req.user, imagen=informacion["imagen"])
            avatar.save()

            return render (req,"inicio.html",{"mensaje":"El avatar se cargo con exito"})
        else:
            return render (req,"inicio.html",{"mensaje":"Datos invalidos"})

    else:
        
        miFormulario = AvatarFormulario()

        return render(req,"agregarAvatar.html",{"miFormulario": miFormulario})
    








