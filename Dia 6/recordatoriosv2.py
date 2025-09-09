import time
import threading
import tkinter as tk
from tkinter import messagebox
from plyer import notification

def recordar(mensaje, delay):
    def tarea():
        time.sleep(delay)
        notification.notify(
            title="🔔 Recordatorio",
            message=mensaje,
            timeout=10
        )
    threading.Thread(target=tarea).start()

def programar():
    try:
        mensaje = entry_mensaje.get()
        delay = int(entry_tiempo.get())
        if mensaje.strip() == "":
            messagebox.showwarning("Error", "El mensaje no puede estar vacío.")
            return
        messagebox.showinfo("Recordatorio programado", f"'{mensaje}' en {delay} segundos.")
        recordar(mensaje, delay)
    except ValueError:
        messagebox.showerror("Error", "El tiempo debe ser un número válido.")

# Interfaz
root = tk.Tk()
root.title("🔔 Recordatorio en Python")
root.geometry("350x200")
root.configure(bg="#1e1e1e")

tk.Label(root, text="Mensaje:", fg="white", bg="#1e1e1e").pack(pady=5)
entry_mensaje = tk.Entry(root, width=40)
entry_mensaje.pack(pady=5)

tk.Label(root, text="Tiempo (segundos):", fg="white", bg="#1e1e1e").pack(pady=5)
entry_tiempo = tk.Entry(root, width=10)
entry_tiempo.pack(pady=5)

btn = tk.Button(root, text="⏰ Recordar", command=programar, bg="#4CAF50", fg="white")
btn.pack(pady=15)

root.mainloop()
