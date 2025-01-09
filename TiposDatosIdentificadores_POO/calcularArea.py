# Este es un programa para calcular el área de un círculo o un rectángulo.
# El usuario puede elegir la figura, ingresar las dimensiones y obtener el resultado.

import math


def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    return math.pi * radio ** 2


def calcular_area_rectangulo(largo, ancho):
    """Calcula el área de un rectángulo dado su largo y ancho."""
    return largo * ancho


def main():
    print("Calculadora de áreas")
    continuar = True

    while continuar:
        print("\nElige una opción:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")

        try:
            opcion = int(input("Introduce el número de la opción deseada: "))

            if opcion == 1:
                radio = float(input("Introduce el radio del círculo: "))
                area = calcular_area_circulo(radio)
                print(f"El área del círculo con radio {radio} es {area:.2f}")

            elif opcion == 2:
                largo = float(input("Introduce el largo del rectángulo: "))
                ancho = float(input("Introduce el ancho del rectángulo: "))
                area = calcular_area_rectangulo(largo, ancho)
                print(f"El área del rectángulo de {largo} x {ancho} es {area:.2f}")

            else:
                print("Opción no válida. Intenta de nuevo.")

        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")

        seguir = input("¿Quieres realizar otro cálculo? (sí/no): ").strip().lower()
        continuar = seguir == 'sí'

    print("Gracias por usar la calculadora de áreas. ¡Hasta pronto!")


if __name__ == "__main__":
    main()
