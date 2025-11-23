import tkinter as tk
from tkinter import messagebox, filedialog
import speech_recognition as sr

# https://github.com/lucmadev/30-Dias-de-Python

# pip install SpeechRecognition pyaudio

# si no deja instalar pyAudio en Windows:
# pip install pipwin
# pipwin install pyaudio

# --- Funciones ---
def guardar_nota():
    texto = text_area.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showwarning("Aviso", "No hay texto para guardar.")
        return

    archivo = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt")]
    )
    if archivo:
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(texto)
        messagebox.showinfo("Éxito", f"Nota guardada en {archivo}")

def cargar_nota():
    archivo = filedialog.askopenfilename(
        filetypes=[("Archivos de texto", "*.txt")]
    )
    if archivo:
        with open(archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, contenido)

def transcribir_voz():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("Habla ahora", "Empieza a hablar...")
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language="es-ES")
        text_area.insert(tk.END, texto + "\n")
    except sr.UnknownValueError:
        messagebox.showerror("Error", "No entendí lo que dijiste")
    except sr.RequestError:
        messagebox.showerror("Error", "No se pudo conectar con el servicio de reconocimiento.")

# --- Interfaz ---
root = tk.Tk()
root.title("📝 App de Notas con Voz")

frame = tk.Frame(root)
frame.pack(pady=10)

btn_guardar = tk.Button(frame, text="Guardar", command=guardar_nota)
btn_guardar.grid(row=0, column=0, padx=5)

btn_cargar = tk.Button(frame, text="Cargar", command=cargar_nota)
btn_cargar.grid(row=0, column=1, padx=5)

btn_voz = tk.Button(frame, text="Dictar nota", command=transcribir_voz)
btn_voz.grid(row=0, column=2, padx=5)

text_area = tk.Text(root, width=50, height=15)
text_area.pack(pady=10)

root.mainloop()
