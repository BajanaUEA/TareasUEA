# Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        :param id: ID único del producto.
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad disponible del producto.
        :param precio: Precio del producto.
        """
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        """
        Representación en cadena del producto.
        """
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


# Clase Inventario
class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa una lista vacía para almacenar los productos.
        """
        self.productos = []

    def agregar_producto(self, producto):
        """
        Añade un nuevo producto al inventario.
        :param producto: Objeto de la clase Producto.
        """
        # Verificar si el ID ya existe
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID ya existe.")
        else:
            self.productos.append(producto)
            print("Producto añadido correctamente.")

    def eliminar_producto(self, id):
        """
        Elimina un producto por su ID.
        :param id: ID del producto a eliminar.
        """
        for producto in self.productos:
            if producto.get_id() == id:
                self.productos.remove(producto)
                print("Producto eliminado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto por su ID.
        :param id: ID del producto a actualizar.
        :param cantidad: Nueva cantidad (opcional).
        :param precio: Nuevo precio (opcional).
        """
        for producto in self.productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print("Producto actualizado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        """
        Busca productos por nombre (puede haber nombres similares).
        :param nombre: Nombre del producto a buscar.
        :return: Lista de productos que coinciden con el nombre.
        """
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        """
        Muestra todos los productos en el inventario.
        """
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")


# Interfaz de Usuario en la Consola
def menu():
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = int(input("Ingrese el ID del producto a actualizar: "))
            cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecutar el programa
if __name__ == "__main__":
    menu()