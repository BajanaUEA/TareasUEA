import tkinter as tk
from tkinter import messagebox

# Función para agregar información a la lista
def agregar_info():
    info = campo_texto.get()  # Obtener el texto del campo de entrada
    if info:  # Verificar que el campo no esté vacío
        lista.insert(tk.END, info)  # Agregar la información al final de la lista
        campo_texto.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Campo vacío", "Por favor, ingrese información.")

# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)  # Borrar todos los elementos de la lista

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")  # Título de la ventana

# Crear y colocar los componentes en la ventana
etiqueta = tk.Label(ventana, text="Ingrese su información:")
etiqueta.pack(pady=10)  # Espaciado vertical

campo_texto = tk.Entry(ventana, width=40)
campo_texto.pack(pady=5)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_info)
boton_agregar.pack(pady=5)

lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=10)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()