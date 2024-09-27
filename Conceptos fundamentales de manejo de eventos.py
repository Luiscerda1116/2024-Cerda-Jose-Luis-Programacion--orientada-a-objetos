import tkinter as tk
from tkinter import ttk

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x300")

        self.tareas = []

        # Campo de entrada
        self.entrada_tarea = ttk.Entry(root, width=40)
        self.entrada_tarea.grid(row=0, column=0, padx=5, pady=5)
        self.entrada_tarea.bind("<Return>", self.anadir_tarea)

        # Botón Añadir Tarea
        self.btn_anadir = ttk.Button(root, text="Añadir Tarea", command=self.anadir_tarea)
        self.btn_anadir.grid(row=0, column=1, padx=5, pady=5)

        # Lista de tareas
        self.lista_tareas = tk.Listbox(root, width=50, height=10)
        self.lista_tareas.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.lista_tareas.bind("<Double-1>", self.marcar_completada)

        # Botón Marcar como Completada
        self.btn_completar = ttk.Button(root, text="Marcar como Completada", command=self.marcar_completada)
        self.btn_completar.grid(row=2, column=0, padx=5, pady=5)

        # Botón Eliminar Tarea
        self.btn_eliminar = ttk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_eliminar.grid(row=2, column=1, padx=5, pady=5)

    def anadir_tarea(self, event=None):
        tarea = self.entrada_tarea.get()
        if tarea:
            self.tareas.append({"texto": tarea, "completada": False})
            self.actualizar_lista()
            self.entrada_tarea.delete(0, tk.END)

    def marcar_completada(self, event=None):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            self.tareas[indice]["completada"] = not self.tareas[indice]["completada"]
            self.actualizar_lista()

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            del self.tareas[indice]
            self.actualizar_lista()

    def actualizar_lista(self):
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            texto = tarea["texto"]
            if tarea["completada"]:
                texto = "✓ " + texto
            self.lista_tareas.insert(tk.END, texto)

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()