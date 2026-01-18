import tkinter as tk
import time

# https://github.com/lucmadev/30-Dias-de-Python

running = False
start_time = 0
elapsed_time = 0

def start():
    global running, start_time
    if not running:
        start_time = time.time() - elapsed_time
        update_time()
        running = True

def pause():
    global running, elapsed_time
    if running:
        root.after_cancel(update_job)
        elapsed_time = time.time() - start_time
        running = False

def reset():
    global running, elapsed_time
    running = False
    elapsed_time = 0
    label.config(text="00:00:00")
    laps_list.delete(0, tk.END)

def lap():
    if running:
        current_time = time.time() - start_time
    else:
        current_time = elapsed_time
    h, m, s = int(current_time // 3600), int((current_time % 3600) // 60), int(current_time % 60)
    laps_list.insert(tk.END, f"{h:02}:{m:02}:{s:02}")

def update_time():
    global elapsed_time, update_job
    elapsed_time = time.time() - start_time
    h, m, s = int(elapsed_time // 3600), int((elapsed_time % 3600) // 60), int(elapsed_time % 60)
    label.config(text=f"{h:02}:{m:02}:{s:02}")
    update_job = root.after(1000, update_time)

# --- Interfaz ---
root = tk.Tk()
root.title("⏱️ Cronómetro Mejorado")

label = tk.Label(root, text="00:00:00", font=("Arial", 40))
label.pack(pady=20)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="▶️ Start", command=start).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="⏸️ Pause", command=pause).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="🔄 Reset", command=reset).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="🏁 Lap", command=lap).grid(row=0, column=3, padx=5)

laps_list = tk.Listbox(root, width=20, height=5)
laps_list.pack(pady=10)

root.mainloop()
