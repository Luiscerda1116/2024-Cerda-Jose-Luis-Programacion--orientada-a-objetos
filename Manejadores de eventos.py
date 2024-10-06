import tkinter as tk
from tkinter import ttk

class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestor de Tareas")
        self.master.geometry("400x300")

        self.tasks = []

        # Campo de entrada
        self.task_entry = ttk.Entry(self.master, width=30)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        # Botones
        self.add_button = ttk.Button(self.master, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.complete_button = ttk.Button(self.master, text="Completar Tarea", command=self.complete_task)
        self.complete_button.grid(row=1, column=0, padx=5, pady=5)

        self.delete_button = ttk.Button(self.master, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=1, column=1, padx=5, pady=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(self.master, width=50, height=10)
        self.task_listbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Atajos de teclado
        self.master.bind('<Return>', lambda event: self.add_task())
        self.master.bind('c', lambda event: self.complete_task())
        self.master.bind('<Delete>', lambda event: self.delete_task())
        self.master.bind('<d>', lambda event: self.delete_task())
        self.master.bind('<Escape>', lambda event: self.master.quit())

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"text": task, "completed": False})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)

    def complete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index]["completed"] = True
            self.update_task_list()
        except IndexError:
            pass

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.update_task_list()
        except IndexError:
            pass

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            prefix = "✓ " if task["completed"] else "• "
            self.task_listbox.insert(tk.END, prefix + task["text"])
            if task["completed"]:
                self.task_listbox.itemconfig(tk.END, {'fg': 'gray'})

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()