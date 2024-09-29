# Creando el diccionario con información personal
informacion_personal = {
    "nombre": "Juan Pérez",  # Nombre de la persona
    "edad": 30,              # Edad de la persona
    "ciudad": "Quito",       # Ciudad de residencia
    "profesion": "Ingeniero" # Profesión de la persona
}

# Accediendo al valor de la clave "ciudad" y modificándola
informacion_personal["ciudad"] = "Guayaquil"  # Cambiando la ciudad a Guayaquil

# Agregando una nueva clave-valor para "profesion"
informacion_personal["profesion"] = "Desarrollador de Software"  # Actualizando la profesión

# Verificando si la clave "telefono" existe, si no, la agregamos
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0991234567"  # Agregando un número de teléfono ficticio

# Eliminando la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]  # Eliminando la edad del diccionario

# Imprimiendo el diccionario resultante
print(informacion_personal)
