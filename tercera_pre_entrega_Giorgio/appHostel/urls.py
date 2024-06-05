from django.contrib import admin
from django.urls import path
from appHostel.views import cuartos ,clientes ,empleados, inicio, agregar_cuarto, agregar_cliente, agregar_empleado, lista_empleado, buscar_puesto, buscar


urlpatterns = [
    
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
]