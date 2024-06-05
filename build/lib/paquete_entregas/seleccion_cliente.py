

def seleccion_cliente(lista_de_clientes):
    print("Los clientes ingresados son: ")
    for i, posicion_cliente in enumerate(lista_de_clientes, start = 1):
        print(f"{i} - {posicion_cliente}")
    cliente_a_seleccionar = int(input("Debe seleccionar un cliente: "))
    cliente_seleccionado =  lista_de_clientes [cliente_a_seleccionar - 1]
    print(f"Usted selecciono a: {cliente_seleccionado}")
    return cliente_seleccionado 



   



