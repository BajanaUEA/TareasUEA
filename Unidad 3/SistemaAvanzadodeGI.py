import json
import os

# Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos (clave: ID, valor: Producto)

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.id] = producto
            print(f"Producto '{producto.nombre}' agregado correctamente.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print(f"Producto con ID {id} eliminado correctamente.")
        else:
            print("Error: No existe un producto con ese ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print(f"Producto con ID {id} actualizado correctamente.")
        else:
            print("Error: No existe un producto con ese ID.")

    def buscar_por_nombre(self, nombre):
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.nombre.lower()]
        if resultados:
            print("Resultados de la búsqueda:")
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if self.productos:
            print("Inventario actual:")
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

# Funciones para guardar y cargar el inventario desde un archivo
def guardar_inventario(inventario, archivo="inventario.json"):
    with open(archivo, "w") as f:
        datos = {id: {"nombre": producto.nombre, "cantidad": producto.cantidad, "precio": producto.precio}
                 for id, producto in inventario.productos.items()}
        json.dump(datos, f)
    print(f"Inventario guardado en '{archivo}'.")

def cargar_inventario(archivo="inventario.json"):
    inventario = Inventario()
    if os.path.exists(archivo):
        with open(archivo, "r") as f:
            datos = json.load(f)
            for id, info in datos.items():
                producto = Producto(id, info["nombre"], info["cantidad"], info["precio"])
                inventario.agregar_producto(producto)
        print(f"Inventario cargado desde '{archivo}'.")
    else:
        print(f"El archivo '{archivo}' no existe. Se creará uno nuevo al guardar.")
    return inventario

# Menú interactivo
def menu():
    inventario = cargar_inventario()
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar y salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje vacío para no cambiar): ")
            precio = input("Ingrese el nuevo precio (deje vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            guardar_inventario(inventario)
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
