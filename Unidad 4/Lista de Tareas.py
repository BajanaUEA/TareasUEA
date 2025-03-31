import tkinter as tk
from tkinter import messagebox, ttk


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("500x400")

        # Configurar estilo
        self.style = ttk.Style()
        self.style.configure("Completed.TLabel", foreground="gray", font=('Arial', 10, 'overstrike'))
        self.style.configure("Normal.TLabel", foreground="black", font=('Arial', 10))

        # Frame principal
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Entrada de tarea
        self.task_entry = ttk.Entry(self.main_frame, font=('Arial', 12))
        self.task_entry.pack(fill=tk.X, pady=(0, 10))
        self.task_entry.bind("<Return>", lambda e: self.add_task())

        # Botones
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(fill=tk.X, pady=(0, 10))

        self.add_button = ttk.Button(self.button_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, expand=True, padx=2)

        self.complete_button = ttk.Button(self.button_frame, text="Marcar como Completada",
                                          command=self.mark_completed)
        self.complete_button.pack(side=tk.LEFT, expand=True, padx=2)

        self.delete_button = ttk.Button(self.button_frame, text="Eliminar Tarea",
                                        command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, expand=True, padx=2)

        # Lista de tareas
        self.tasks_frame = ttk.Frame(self.main_frame)
        self.tasks_frame.pack(fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.tasks_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tasks_list = tk.Listbox(
            self.tasks_frame,
            yscrollcommand=self.scrollbar.set,
            font=('Arial', 12),
            selectmode=tk.SINGLE,
            activestyle="none",
            highlightthickness=0,
            bd=0
        )
        self.tasks_list.pack(fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.tasks_list.yview)

        # Evento de doble clic para marcar como completada
        self.tasks_list.bind("<Double-Button-1>", lambda e: self.mark_completed())

        # Almacenar estado de las tareas
        self.tasks = []

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({"text": task_text, "completed": False})
            self.update_tasks_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea válida.")

    def mark_completed(self):
        selected_index = self.tasks_list.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_tasks_list()

    def delete_task(self):
        selected_index = self.tasks_list.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_tasks_list()

    def update_tasks_list(self):
        self.tasks_list.delete(0, tk.END)
        for task in self.tasks:
            if task["completed"]:
                self.tasks_list.insert(tk.END, task["text"])
                self.tasks_list.itemconfig(tk.END, {'fg': 'gray'})
            else:
                self.tasks_list.insert(tk.END, task["text"])
                self.tasks_list.itemconfig(tk.END, {'fg': 'black'})


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()