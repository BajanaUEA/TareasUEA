import tkinter as tk
from tkinter import ttk, messagebox


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("500x400")

        # Configurar atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<c>', lambda event: self.mark_completed())
        self.root.bind('<C>', lambda event: self.mark_completed())
        self.root.bind('<d>', lambda event: self.delete_task())
        self.root.bind('<D>', lambda event: self.delete_task())
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('<Escape>', lambda event: self.root.quit())

        # Crear la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Frame para entrada de nueva tarea
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=10, padx=10, fill=tk.X)

        self.task_entry = ttk.Entry(input_frame, font=('Arial', 12))
        self.task_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.task_entry.focus()

        add_button = ttk.Button(input_frame, text="Añadir (Enter)", command=self.add_task)
        add_button.pack(side=tk.LEFT, padx=5)

        # Frame para botones de acción
        action_frame = ttk.Frame(self.root)
        action_frame.pack(pady=5, padx=10, fill=tk.X)

        complete_button = ttk.Button(action_frame, text="Completar (C)", command=self.mark_completed)
        complete_button.pack(side=tk.LEFT, expand=True)

        delete_button = ttk.Button(action_frame, text="Eliminar (D/Delete)", command=self.delete_task)
        delete_button.pack(side=tk.LEFT, expand=True, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(
            self.root,
            font=('Arial', 12),
            selectbackground="#a6a6a6",
            selectmode=tk.SINGLE,
            height=15
        )
        self.task_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Barra de desplazamiento
        scrollbar = ttk.Scrollbar(self.task_listbox)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.task_listbox.insert(tk.END, task_text)
            self.task_listbox.itemconfig(tk.END, fg="black")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese una tarea.")

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.itemconfig(selected_index, fg="green")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()