
# https://github.com/lucmadev/30-Dias-de-Python
import tkinter as tk
import time
import random

oraciones = [
    "El conocimiento es poder.",
    "Python es un lenguaje increíble.",
    "Aprender código cambia tu forma de pensar.",
    "La práctica hace al maestro.",
    "Nunca pares de crear."
]

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medidor de Velocidad al Tipear ⌨️")
        self.root.geometry("500x300")

        self.texto = tk.StringVar(value=random.choice(oraciones))
        self.start_time = None

        tk.Label(root, text="Escribí la siguiente oración:", font=("Arial", 12)).pack(pady=10)
        self.frase = tk.Label(root, textvariable=self.texto, font=("Arial", 14), wraplength=400)
        self.frase.pack(pady=5)

        self.entry = tk.Entry(root, font=("Arial", 12), width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<KeyPress>", self.start_timer)

        self.boton = tk.Button(root, text="Ver resultado", command=self.calcular_velocidad)
        self.boton.pack(pady=10)

        self.resultado = tk.Label(root, text="", font=("Arial", 12))
        self.resultado.pack(pady=10)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def calcular_velocidad(self):
        if not self.start_time:
            return

        elapsed_time = time.time() - self.start_time
        texto_usuario = self.entry.get()
        palabras = len(texto_usuario.split())
        wpm = round(palabras / (elapsed_time / 60), 2)

        original = self.texto.get()
        correctas = sum(1 for a, b in zip(original, texto_usuario) if a == b)
        precision = round((correctas / len(original)) * 100, 2)

        self.resultado.config(text=f"⏱️ {wpm} WPM | 🎯 Precisión: {precision}%")
        self.start_time = None
        self.entry.delete(0, tk.END)
        self.texto.set(random.choice(oraciones))

root = tk.Tk()
app = TypingSpeedApp(root)
root.mainloop()
