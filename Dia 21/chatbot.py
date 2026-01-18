import random

# https://github.com/lucmadev/30-Dias-de-Python

respuestas = {
    "hola": ["¡Hola! ¿Cómo estás?", "Buenas buenas 👋", "¡Hey! ¿Todo piola?"],
    "tiempo": ["El clima está perfecto para codear ☀️", "Parece que va a llover código hoy ⛈️"],
    "chiste": [
        "¿Qué le dice un bit al otro? Nos vemos en el bus 😂",
        "Mi vida es como un array: sin orden… pero con propósito."
    ],
    "adios": ["¡Nos vemos! 👋", "Chau chau, no te olvides de guardar 😎"]
}

def responder(mensaje):
    mensaje = mensaje.lower()

    for clave in respuestas:
        if clave in mensaje:
            return random.choice(respuestas[clave])
    
    return "No entendí eso, pero suena interesante 🤔"

print("🤖 Chatbot iniciado. Escribí 'salir' para terminar.\n")

while True:
    user = input("Vos: ")

    if user.lower() == "salir":
        print("Bot: ¡Hasta luego! 🤖")
        break

    print("Bot:", responder(user))
