import tkinter as tk
from tkinter import filedialog, messagebox

def guardar():
    nota = text.get("1.0", tk.END).strip()
    if nota:
        archivo = filedialog.asksaveasfilename(defaultextension=".txt",
                                               filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            with open(archivo, "w", encoding="utf-8") as f:
                f.write(nota)
            messagebox.showinfo("Notas", "✅ Nota guardada correctamente")
    else:
        messagebox.showwarning("Notas", "No hay nada para guardar.")

def cargar():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        with open(archivo, "r", encoding="utf-8") as f:
            nota = f.read()
        text.delete("1.0", tk.END)
        text.insert(tk.END, nota)
        messagebox.showinfo("Notas", "📂 Nota cargada correctamente")

# Interfaz
root = tk.Tk()
root.title("📝 Tomador de Notas en Python")
root.geometry("400x400")
root.configure(bg="#1e1e1e")

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

btn_guardar = tk.Button(frame, text="💾 Guardar", command=guardar, bg="#4CAF50", fg="white")
btn_guardar.grid(row=0, column=0, padx=5)

btn_cargar = tk.Button(frame, text="📂 Cargar", command=cargar, bg="#2196F3", fg="white")
btn_cargar.grid(row=0, column=1, padx=5)

text = tk.Text(root, wrap="word", width=40, height=15, bg="#2d2d2d", fg="white", insertbackground="white")
text.pack(pady=10)

root.mainloop()
