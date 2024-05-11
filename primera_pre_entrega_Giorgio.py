

usuarios = {}


#Funcion de registro:

def registrar_un_usuario(base_de_datos):
    nombre_usuario = input("Ingrese el nombre de usuario: ").strip()
    contrasena = input("Ingrese contrasena: ").strip()
    if nombre_usuario == "" or contrasena == "":
       print("Nombre o contrasena no puede estar vacios")
    else:         
     base_de_datos[nombre_usuario] = contrasena
     print("El usuario se cargo correctamente")


#Funcion para mostrar los usuarios:

def mostrar_usuario(base_de_datos):
    print("Usuarios registrados:")
    if len(base_de_datos) == 0:
       print("No hay usuarios ingresados")
    else:   
       for usuario, contrasena in base_de_datos.items():
        print(f"nombre_usuario: {usuario}, contrasena: {contrasena}")


#Funcion para login:

def login(base_de_datos):
    nombre_usuario = input("Ingrese nombre de usuario: ")
    contrasena = input("Ingrese contrasena: ")
    if nombre_usuario in base_de_datos and base_de_datos[nombre_usuario] == contrasena:
        print("Ingreso correctamente")
    else:
        print("Usuario o contrasena no son validos. Vuelva a intentarlo.")    


#Menu:

while True:
    print("1. Registrar usuario")
    print("2. Mostrar usuarios")
    print("3. Login")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_un_usuario(usuarios)
    elif opcion == "2":
        mostrar_usuario(usuarios)
    elif opcion == "3":
        login(usuarios)
    elif opcion == "4":
        print("Hasta la proxima..")
        break
    else:
        print("Opcion no valida, seleccione una opcion valida.")





















