import os

carpeta = r"D:\PROYECTOS\Python\30DiasDePython\Dia 10\archivos"

nuevo_nombre = "foto_"

extension = ".png"

def renombrar_archivos():
    archivos = [f for f in os.listdir(carpeta) if f.endswith(extension)]
    
    for i, archivo in enumerate(archivos, start=1):
        ruta_vieja = os.path.join(carpeta, archivo)
        ruta_nueva = os.path.join(carpeta, f"{nuevo_nombre}{i}{extension}")
        os.rename(ruta_vieja, ruta_nueva)
        print(f"✅ {archivo} → {nuevo_nombre}{i}{extension}")

    print("\n🎉 Renombrado masivo completado.")

renombrar_archivos()
