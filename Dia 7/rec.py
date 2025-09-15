import speech_recognition as sr

# Inicializar reconocedor
r = sr.Recognizer()

# Usar el micrófono como fuente de audio
with sr.Microphone() as source:
    print("🎤 Habla algo (estoy escuchando)...")
    audio = r.listen(source)

    try:
        # Reconocimiento usando Google
        texto = r.recognize_google(audio, language="es-ES")
        print("📝 Texto reconocido: " + texto)
    except sr.UnknownValueError:
        print("❌ No se entendió lo que dijiste")
    except sr.RequestError:
        print("⚠️ Error con el servicio de Google")
