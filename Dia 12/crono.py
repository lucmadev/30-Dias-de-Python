import tkinter as tk

# Variables globales
running = False
counter = 0

def start():
    global running
    if not running:
        running = True
        run_timer()

def stop():
    global running
    running = False

def reset():
    global counter, running
    running = False
    counter = 0
    label.config(text="00:00:00")

def run_timer():
    global counter
    if running:
        counter += 1
        horas = counter // 3600
        minutos = (counter % 3600) // 60
        segundos = counter % 60
        label.config(text=f"{horas:02}:{minutos:02}:{segundos:02}")
        root.after(1000, run_timer)

# Interfaz
root = tk.Tk()
root.title("⏱ Cronómetro")
root.geometry("300x200")
root.configure(bg="#1e1e1e")

label = tk.Label(root, text="00:00:00", font=("Arial", 30), fg="lime", bg="#1e1e1e")
label.pack(pady=20)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

btn_start = tk.Button(frame, text="▶ Iniciar", command=start, bg="#4CAF50", fg="white")
btn_start.grid(row=0, column=0, padx=5)

btn_stop = tk.Button(frame, text="⏸ Pausar", command=stop, bg="#f44336", fg="white")
btn_stop.grid(row=0, column=1, padx=5)

btn_reset = tk.Button(frame, text="🔄 Reiniciar", command=reset, bg="#2196F3", fg="white")
btn_reset.grid(row=0, column=2, padx=5)

root.mainloop()
