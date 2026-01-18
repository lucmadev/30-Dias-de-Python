# https://github.com/lucmadev/30-Dias-de-Python

# pip install cryptography

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generar_claves_simple(bits: int = 2048, passphrase: bytes | None = None):
    # Genera clave privada
    clave_privada = rsa.generate_private_key(public_exponent=65537, key_size=bits)

    # Serializa privada (PEM) — encriptada si pasas passphrase
    enc = serialization.BestAvailableEncryption(passphrase) if passphrase else serialization.NoEncryption()
    pem_priv = clave_privada.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=enc
    )

    # Serializa pública (PEM)
    clave_publica = clave_privada.public_key()
    pem_pub = clave_publica.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return pem_priv, pem_pub

if __name__ == "__main__":
    # Generar claves
    priv_pem, pub_pem = generar_claves_simple(bits=2048)

    # Guardar archivos
    with open("rsa_priv.pem", "wb") as f:
        f.write(priv_pem)
    with open("rsa_pub.pem", "wb") as f:
        f.write(pub_pem)

    print("🔐 Claves generadas y guardadas:")
    print(" - rsa_priv.pem  (clave privada)")
    print(" - rsa_pub.pem   (clave pública)")
    print("\n⚠️ Guarda la clave privada en un lugar seguro. La pública podés compartirla.")
