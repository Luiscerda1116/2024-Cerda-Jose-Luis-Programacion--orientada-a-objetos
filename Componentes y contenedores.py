import pip

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Necesario instalar tkcalendar (pip install tkcalendar)

# Clase principal de la aplicación
class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Crear el marco principal
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        # Campos de entrada para agregar eventos
        tk.Label(frame, text="Fecha").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(frame, width=12, background='darkblue',
                                    foreground='white', borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Hora").grid(row=1, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(frame)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Descripción").grid(row=2, column=0, padx=5, pady=5)
        self.description_entry = tk.Entry(frame)
        self.description_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botones para agregar y eliminar eventos
        add_button = tk.Button(frame, text="Agregar Evento", command=self.add_event)
        add_button.grid(row=3, column=0, padx=5, pady=5)

        delete_button = tk.Button(frame, text="Eliminar Evento", command=self.delete_event)
        delete_button.grid(row=3, column=1, padx=5, pady=5)

        # Lista de eventos (Treeview)
        self.tree = ttk.Treeview(self.root, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(padx=10, pady=10)

        # Botón de salir
        exit_button = tk.Button(self.root, text="Salir", command=self.root.quit)
        exit_button.pack(pady=5)

    def add_event(self):
        # Obtener los datos del usuario
        date = self.date_entry.get()
        time = self.time_entry.get()
        description = self.description_entry.get()

        if not date or not time or not description:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return

        # Agregar evento a la lista (Treeview)
        self.tree.insert("", tk.END, values=(date, time, description))

        # Limpiar los campos de entrada
        self.time_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

    def delete_event(self):
        selected_item = self.tree.selection()
        if selected_item:
            # Confirmar eliminación
            confirm = messagebox.askyesno("Confirmar", "¿Deseas eliminar el evento seleccionado?")
            if confirm:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar")


# Inicializar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()




