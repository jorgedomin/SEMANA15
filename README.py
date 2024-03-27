import tkinter as tk

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        self.tareas = []

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        # Botón para añadir tarea
        self.btn_agregar = tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea)
        self.btn_agregar.pack()

        # Lista de tareas
        self.lista_tareas = tk.Listbox(root, width=50)
        self.lista_tareas.pack(pady=10)

        # Botón para marcar como completada
        self.btn_completar = tk.Button(root, text="Marcar como Completada", command=self.marcar_como_completada)
        self.btn_completar.pack()

        # Botón para eliminar tarea
        self.btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_eliminar.pack()

        # Enlazar la tecla Enter al campo de entrada para añadir tarea
        self.entry.bind("<Return>", lambda event: self.agregar_tarea())

    def agregar_tarea(self):
        tarea = self.entry.get()
        if tarea:
            self.tareas.append(tarea)
            self.lista_tareas.insert(tk.END, tarea)
            self.entry.delete(0, tk.END)  # Limpiar el campo de entrada después de añadir una tarea

    def marcar_como_completada(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            index = seleccion[0]
            tarea = self.lista_tareas.get(index)
            tarea_completada = tarea + " - COMPLETADA"
            self.lista_tareas.delete(index)
            self.lista_tareas.insert(index, tarea_completada)

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            index = seleccion[0]
            self.lista_tareas.delete(index)
            del self.tareas[index]

def main():
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
