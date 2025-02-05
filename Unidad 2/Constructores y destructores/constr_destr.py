# Definición de la clase Archivo
class Archivo:
    def __init__(self, nombre_archivo):
        """
        Constructor de la clase Archivo.
        Se ejecuta automáticamente al crear una instancia de la clase.
        Inicializa el archivo y lo abre en modo lectura.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(nombre_archivo, 'r')  # Abre el archivo en modo lectura
        print(f"Archivo '{self.nombre_archivo}' abierto correctamente.")

    def leer(self):
        """
        Metodo para leer el contenido del archivo.
        """
        print(f"Leyendo el archivo '{self.nombre_archivo}':")
        print(self.archivo.read())  # Lee y muestra el contenido del archivo

    def __del__(self):
        """
        Destructor de la clase Archivo.
        Se ejecuta automáticamente cuando el objeto es eliminado.
        Cierra el archivo para liberar recursos.
        """
        if hasattr(self, 'archivo') and not self.archivo.closed:
            self.archivo.close()  # Cierra el archivo si está abierto
            print(f"Archivo '{self.nombre_archivo}' cerrado correctamente.")
        else:
            print(f"El archivo '{self.nombre_archivo}' ya estaba cerrado.")

# Uso de la clase Archivo
if __name__ == "__main__":
    # Crear una instancia de la clase Archivo
    archivo = Archivo("ejemplo.txt")  # Se llama al constructor __init__

    # Leer el contenido del archivo
    archivo.leer()

    # Eliminar la referencia al objeto (llama al destructor __del__)
    del archivo