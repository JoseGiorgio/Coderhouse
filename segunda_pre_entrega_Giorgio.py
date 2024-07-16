
from paquete_entregas.cliente import Cliente
from paquete_entregas.seleccion_cliente import seleccion_cliente

   



lista_de_clientes = [

 Cliente("Jose", "Liniers", "josecho@gmail.com"),
 Cliente("David", "Almagro", "davichin@gmail.com"),
 Cliente("Nicolas", "Funes", "nicolas94@gmail.com"),

]


cliente_seleccionado = seleccion_cliente (lista_de_clientes)

while True:
    print(" - Elija una opcion: -")
    print("1 - Ingrese un producto: ")
    print("2 - Elimine un producto: ")
    print("3 - Mostrar compras: ")
    print("4 - Cambiar de cliente: ")
    print("5 - Salir: ")

    opcion = input("Por favor, ingrese una opcion: ")

    if opcion == "1":
        producto = input("Agregar producto: ").strip().capitalize()
        if producto == "":
            print("Debe agregar un producto.")
        else:
            cliente_seleccionado.ingreso_de_compra(producto)
    elif opcion == "2":
        producto = input("Eliminar producto: ").strip().capitalize()
        if producto == "":
            print("No se ingreso ningun producto.")
        else:
            cliente_seleccionado.quitar_compra(producto)
    elif opcion == "3":
        cliente_seleccionado.mostrar_compras()
    elif opcion == "4":
        cliente_seleccionado = seleccion_cliente (lista_de_clientes)    
    elif opcion == "5":
        print("Hasta la proxima.")
        break
    else:
        print("La opcion es invalida. ")                    
    





















