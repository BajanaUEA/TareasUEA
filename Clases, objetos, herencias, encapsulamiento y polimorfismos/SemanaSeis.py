# Aplicación de Conceptos de POO en Python

# Clase base
class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo encapsulado
        self.__edad = edad      # Atributo encapsulado

    # Getter para el nombre
    def get_nombre(self):
        return self.__nombre

    # Getter para la edad
    def get_edad(self):
        return self.__edad

    # Método genérico
    def hacer_sonido(self):
        return "El animal hace un sonido."

# Clase derivada (Herencia)
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.raza = raza  # Atributo específico de la clase derivada

    # Sobrescritura de método (Polimorfismo)
    def hacer_sonido(self):
        return "El perro ladra."

    # Método específico de la clase derivada
    def mostrar_info(self):
        return f"Nombre: {self.get_nombre()}, Edad: {self.get_edad()}, Raza: {self.raza}"

# Clase derivada adicional (Demostración de polimorfismo)
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color  # Atributo específico de la clase derivada

    # Sobrescritura de método (Polimorfismo)
    def hacer_sonido(self):
        return "El gato maúlla."

    # Método específico de la clase derivada
    def mostrar_info(self):
        return f"Nombre: {self.get_nombre()}, Edad: {self.get_edad()}, Color: {self.color}"

# Crear instancias de las clases
perro = Perro("Rex", 5, "Labrador")
gato = Gato("Michi", 3, "Blanco")

# Demostración de encapsulación y acceso a atributos mediante getters
print(perro.mostrar_info())  # Salida: Nombre: Rex, Edad: 5, Raza: Labrador
print(gato.mostrar_info())  # Salida: Nombre: Michi, Edad: 3, Color: Blanco

# Demostración de polimorfismo
animales = [perro, gato]
for animal in animales:
    print(animal.hacer_sonido())  # Salida: "El perro ladra." y "El gato maúlla."
