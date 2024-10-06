# Escritura de Archivo de Texto
# Creamos un archivo llamado my_notes.txt y escribimos tres líneas de notas personales.
with open('my_notes.txt', 'w') as file:  # 'w' abre el archivo en modo de escritura (write)
    file.write("Primera línea de notas personales.\n")
    file.write("Segunda línea de notas personales.\n")
    file.write("Tercera línea de notas personales.\n")

# Lectura de Archivo de Texto
# Abrimos el archivo my_notes.txt para leer su contenido línea por línea.
with open('my_notes.txt', 'r') as file:  # 'r' abre el archivo en modo de lectura (read)
    print("Contenido del archivo my_notes.txt:")
    for line in file:  # Itera sobre cada línea del archivo
        print(line.strip())  # Muestra cada línea eliminando los saltos de línea

# El archivo se cierra automáticamente al salir del bloque 'with'
