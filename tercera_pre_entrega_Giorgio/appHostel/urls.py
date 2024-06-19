from django.contrib import admin
from django.urls import path
from appHostel.views import *
from django.contrib.auth.views import LogoutView

urlpatterns =[
    
    path('cuartoFormulario/', agregar_cuarto, name='cuartoFormulario'),
    path('clienteFormulario/', agregar_cliente, name='clienteFormulario'),
    path('empleadoFormulario/', agregar_empleado, name='empleadoFormulario'),
    path("", inicio, name="inicio"),
    path("cuarto/", cuartos, name="cuarto"),
    path("cliente/", clientes, name="cliente"),
    path("empleado/", empleados, name="empleado"),
    path("listaEmpleado/", lista_empleado, name="listaempleado"),
    path("buscarPuesto/", buscar_puesto, name="buscarPuesto"),
    path("buscarEmpleados/", buscar, name="buscarEmpleados"),
    path("editarEmpleado/<int:id>", empleadoEditado, name="editarEmpleado"),
    path("eliminarEmpleado/<int:id>", eliminarEmpleado, name="eliminarEmpleado"),
    path("about/", about, name="about"),
    path("login/", login_view, name="login"),
    path("registrar/", register, name="registrar"),
    path("logout/", LogoutView.as_view(template_name = "logout.html"), name="logout"),
    path("editarPerfil/", editar_perfil, name="editarPerfil"),

]
