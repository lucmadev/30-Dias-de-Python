import tkinter as tk
from tkinter import messagebox
import json
import os

ARCHIVO = "tareas.json"

# Cargar tareas desde archivo, manejo de archivo vacío o corrupto
def cargar_tareas():
    if os.path.exists(ARCHIVO):
        try:
            with open(ARCHIVO, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []

# Guardar tareas en archivo
def guardar_tareas():
    with open(ARCHIVO, "w") as f:
        json.dump(tareas, f)

# Agregar nueva tarea
def agregar_tarea():
    texto = entrada.get().strip()
    if texto:
        tareas.append(texto)
        entrada.delete(0, tk.END)
        actualizar_lista()
        guardar_tareas()
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía")

# Eliminar tarea
def eliminar_tarea(i):
    tareas.pop(i)
    actualizar_lista()
    guardar_tareas()

# Actualizar la lista visual
def actualizar_lista():
    for widget in lista_frame.winfo_children():
        widget.destroy()
    for i, tarea in enumerate(tareas):
        frame = tk.Frame(lista_frame, bg="#1e1e1e")
        tk.Label(frame, text=tarea, bg="#1e1e1e", fg="#ffffff").pack(side="left", padx=5)
        tk.Button(frame, text="❌", command=lambda i=i: eliminar_tarea(i), bg="#333", fg="#fff").pack(side="right")
        frame.pack(fill="x", pady=2)

# --- Configuración de la ventana ---
root = tk.Tk()
root.title("Lista de Tareas")
root.config(bg="#1e1e1e")
root.geometry("400x500")

# Entrada de tarea
entrada = tk.Entry(root, width=40, bg="#333", fg="#fff", insertbackground="white")
entrada.pack(pady=10, padx=10)

# Botón Agregar
tk.Button(root, text="Agregar", command=agregar_tarea, bg="#0f62fe", fg="#fff").pack(pady=5)

# Frame donde se listan las tareas
lista_frame = tk.Frame(root, bg="#1e1e1e")
lista_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Cargar tareas existentes
tareas = cargar_tareas()
actualizar_lista()

root.mainloop()
