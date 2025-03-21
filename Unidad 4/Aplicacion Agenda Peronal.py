import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime
from tkcalendar import Calendar

# Función para agregar un evento
def agregar_evento():
    fecha = calendar.get_date()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if not fecha or not hora or not descripcion:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return

    # Agregar evento al TreeView
    eventos_treeview.insert("", "end", values=(fecha, hora, descripcion))

    # Limpiar los campos de entrada
    entry_hora.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)

# Función para eliminar un evento seleccionado
def eliminar_evento():
    seleccion = eventos_treeview.selection()
    if not seleccion:
        messagebox.showerror("Error", "Por favor, seleccione un evento para eliminar.")
        return

    confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro de que desea eliminar este evento?")
    if confirmacion:
        eventos_treeview.delete(seleccion)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")

# Frame para mostrar la lista de eventos
frame_lista = tk.Frame(ventana)
frame_lista.pack(pady=10)

# TreeView para mostrar los eventos
eventos_treeview = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
eventos_treeview.heading("Fecha", text="Fecha")
eventos_treeview.heading("Hora", text="Hora")
eventos_treeview.heading("Descripción", text="Descripción")
eventos_treeview.pack()

# Frame para los campos de entrada y botones
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

# Etiquetas y campos de entrada
etiqueta_fecha = tk.Label(frame_entrada, text="Fecha:")
etiqueta_fecha.grid(row=0, column=0, padx=5)

calendar = Calendar(frame_entrada, date_pattern="yyyy-mm-dd")
calendar.grid(row=0, column=1, padx=5)

etiqueta_hora = tk.Label(frame_entrada, text="Hora:")
etiqueta_hora.grid(row=1, column=0, padx=5)

entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=5)

etiqueta_descripcion = tk.Label(frame_entrada, text="Descripción:")
etiqueta_descripcion.grid(row=2, column=0, padx=5)

entry_descripcion = tk.Entry(frame_entrada)
entry_descripcion.grid(row=2, column=1, padx=5)

# Botones para agregar y eliminar eventos
boton_agregar = tk.Button(frame_entrada, text="Agregar Evento", command=agregar_evento)
boton_agregar.grid(row=3, column=0, pady=10)

boton_eliminar = tk.Button(frame_entrada, text="Eliminar Evento Seleccionado", command=eliminar_evento)
boton_eliminar.grid(row=3, column=1, pady=10)

# Botón para salir
boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(pady=10)

# Ejecutar la ventana principal
ventana.mainloop()
