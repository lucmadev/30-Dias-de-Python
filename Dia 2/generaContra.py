import random
import string

def generarContraseña(long):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(long))

print("Tu contraseña es: ", generarContraseña(24))