import time
from plyer import notification

def recordar(mensaje, delay):
    print(f"Recordatorio programado: '{mensaje}' en {delay} segundos.")
    time.sleep(delay)
    notification.notify(
        title="🔔 Recordatorio",
        message=mensaje,
        timeout=10
        )
    
recordar("Ver tiktoks de @soylucma", 10)