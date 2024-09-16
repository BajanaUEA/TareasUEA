import numpy as np

# Definir las ciudades, días de la semana y semanas
ciudades = ["Ciudad A", "Ciudad B", "Ciudad C"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4  # Suponiendo 4 semanas


def calcular_promedio_temperaturas(matriz_temperaturas):
    """
    Calcula la temperatura promedio para cada ciudad durante el período dado.

    Args:
    matriz_temperaturas (list of list of list of float): Una matriz 3D donde cada elemento
    representa la temperatura de un día en una semana para una ciudad.

    Returns:
    list of float: Una lista con el promedio de temperaturas para cada ciudad.
    """

    # Número de ciudades (dimensión 0 de la matriz)
    num_ciudades = len(matriz_temperaturas)

    # Inicializar una lista para almacenar el promedio de temperaturas para cada ciudad
    promedios = []

    # Recorrer cada ciudad
    for ciudad in range(num_ciudades):
        # Inicializar variables para acumular la suma de las temperaturas y el número total de días
        suma_temperaturas = 0
        num_dias = 0

        # Recorrer cada semana
        for semana in matriz_temperaturas[ciudad]:
            # Recorrer cada día en la semana
            for temperatura in semana:
                suma_temperaturas += temperatura
                num_dias += 1

        # Calcular el promedio para la ciudad actual
        promedio_ciudad = suma_temperaturas / num_dias if num_dias > 0 else 0
        promedios.append(promedio_ciudad)

    return promedios


# Ejemplo de uso:
# Temperaturas de 3 ciudades durante 4 semanas (cada semana tiene 7 días)
matriz_temperaturas = [
    [  # Ciudad 1
        [30, 32, 34, 31, 30, 29, 30],  # Semana 1
        [31, 33, 35, 32, 30, 29, 31],  # Semana 2
        [32, 34, 36, 33, 31, 30, 32],  # Semana 3
        [33, 35, 37, 34, 32, 31, 33]  # Semana 4
    ],
    [  # Ciudad 2
        [25, 27, 29, 26, 25, 24, 26],  # Semana 1
        [26, 28, 30, 27, 25, 24, 27],  # Semana 2
        [27, 29, 31, 28, 26, 25, 28],  # Semana 3
        [28, 30, 32, 29, 27, 26, 29]  # Semana 4
    ],
    [  # Ciudad 3
        [20, 22, 24, 21, 20, 19, 21],  # Semana 1
        [21, 23, 25, 22, 20, 19, 22],  # Semana 2
        [22, 24, 26, 23, 21, 20, 23],  # Semana 3
        [23, 25, 27, 24, 22, 21, 24]  # Semana 4
    ]
]

# Llamar a la función y mostrar los resultados
promedios = calcular_promedio_temperaturas(matriz_temperaturas)
for i, promedio in enumerate(promedios):
    print(f"Promedio de temperaturas para la Ciudad {i + 1}: {promedio:.2f}°C")

# Crear una matriz 3D para las temperaturas (ciudades, días de la semana, semanas)
# Vamos a suponer que las temperaturas son valores aleatorios entre 15 y 30 grados Celsius
temperaturas = np.random.uniform(low=15, high=30, size=(len(ciudades), len(dias_semana), semanas))

# Calcular el promedio de temperaturas para cada ciudad por cada semana
promedios_semanales = np.zeros((len(ciudades), semanas))

for i in range(len(ciudades)):
    for j in range(semanas):
        # Promedio de temperaturas para la ciudad i en la semana j
        promedio = np.mean(temperaturas[i, :, j])
        promedios_semanales[i, j] = promedio

# Mostrar el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"\nPromedio de temperaturas para {ciudad}:")
    for j in range(semanas):
        print(f"Semana {j+1}: {promedios_semanales[i, j]:.2f} °C")
