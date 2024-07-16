class Cliente():
    def __init__(self, nombre, direccion, email, ):
        self.nombre = nombre
        self.direccion = direccion
        self.email = email 
        self.carrito = []

    def ingreso_de_compra(self, producto):
        self.carrito.append(producto)
        print(f"Usted agrego: {producto} al carrito.")

    def quitar_compra(self, producto):
        if producto in self.carrito: 
            self.carrito.remove(producto)
            print(f"Usted quito: {producto} del carrito.")
        else:
            print("No se encuentra ese articulo en el carrito.")

    def mostrar_compras(self):
        if self.carrito:
            print("Tus compras en el carrito son:")
            for producto in self.carrito:
                print(producto)   
        else:
            print("Usted no tiene productos en el carrito.")                  

    def __str__(self):
        return f"{self.nombre}" 
    



 







 