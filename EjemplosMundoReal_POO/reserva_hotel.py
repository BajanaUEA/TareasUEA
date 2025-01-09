# Clase que representa una habitación de hotel
class Habitacion:
    def __init__(self, numero, tipo, precio, esta_disponible=True):
        """
        Constructor de la clase Habitacion.
        :param numero: Número de la habitación.
        :param tipo: Tipo de la habitación (Ej: "Simple", "Doble").
        :param precio: Precio por noche.
        :param esta_disponible: Disponibilidad de la habitación (True por defecto).
        """
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.esta_disponible = esta_disponible

    def reservar(self):
        """Marca la habitación como no disponible."""
        if self.esta_disponible:
            self.esta_disponible = False
            print(f"Habitación {self.numero} reservada con éxito.")
        else:
            print(f"La habitación {self.numero} ya está reservada.")

    def cancelar_reserva(self):
        """Marca la habitación como disponible."""
        if not self.esta_disponible:
            self.esta_disponible = True
            print(f"La reserva de la habitación {self.numero} ha sido cancelada.")
        else:
            print(f"La habitación {self.numero} ya está disponible.")

# Clase que representa un cliente
class Cliente:
    def __init__(self, nombre, telefono):
        """
        Constructor de la clase Cliente.
        :param nombre: Nombre del cliente.
        :param telefono: Teléfono de contacto del cliente.
        """
        self.nombre = nombre
        self.telefono = telefono

# Clase que representa el sistema de reservas
class SistemaReservas:
    def __init__(self):
        """Constructor de la clase SistemaReservas."""
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        """Agrega una habitación al sistema."""
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        """Muestra todas las habitaciones disponibles."""
        print("Habitaciones disponibles:")
        for habitacion in self.habitaciones:
            if habitacion.esta_disponible:
                print(f"- Habitación {habitacion.numero} ({habitacion.tipo}) - ${habitacion.precio}")

# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Crear algunas habitaciones
    habitacion1 = Habitacion(101, "Simple", 50)
    habitacion2 = Habitacion(102, "Doble", 80)
    habitacion3 = Habitacion(103, "Suite", 150, esta_disponible=False)

    # Crear el sistema de reservas
    sistema = SistemaReservas()
    sistema.agregar_habitacion(habitacion1)
    sistema.agregar_habitacion(habitacion2)
    sistema.agregar_habitacion(habitacion3)

    # Mostrar habitaciones disponibles
    sistema.mostrar_habitaciones_disponibles()

    # Reservar una habitación
    habitacion1.reservar()

    # Intentar reservarla nuevamente
    habitacion1.reservar()

    # Cancelar la reserva
    habitacion1.cancelar_reserva()
