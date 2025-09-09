import tkinter as tk
from tkinter import ttk, messagebox

def convertir():
    try:
        valor = float(entry_valor.get())
        tipo = combo.get()

        if tipo == "Km → Millas":
            resultado = valor * 0.621371
        elif tipo == "Millas → Km":
            resultado = valor / 0.621371
        elif tipo == "°C → °F":
            resultado = (valor * 9/5) + 32
        elif tipo == "°F → °C":
            resultado = (valor - 32) * 5/9
        else:
            resultado = "Conversión no soportada"

        messagebox.showinfo("Resultado", f"✅ {valor} {tipo} = {resultado:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Ingresá un número válido")

# Interfaz
root = tk.Tk()
root.title("🔄 Conversor de Unidades")
root.geometry("300x200")
root.configure(bg="#1e1e1e")

tk.Label(root, text="Valor:", fg="white", bg="#1e1e1e").pack(pady=5)
entry_valor = tk.Entry(root)
entry_valor.pack(pady=5)

tk.Label(root, text="Tipo de conversión:", fg="white", bg="#1e1e1e").pack(pady=5)
combo = ttk.Combobox(root, values=["Km → Millas", "Millas → Km", "°C → °F", "°F → °C"])
combo.pack(pady=5)
combo.current(0)

tk.Button(root, text="Convertir", command=convertir, bg="#4CAF50", fg="white").pack(pady=15)

root.mainloop()