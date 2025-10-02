import requests
from bs4 import BeautifulSoup

url = "https://www.mercadolibre.com.ar/balanza-digital-de-cocina-gadnic-g04-1gr-a-5kg-pro-bascula-gramera/p/MLA19101775#polycard_client=offers&wid=MLA1767339176&sid=offers&deal_print_id=&tracking_id="

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

precio_objetivo = 16000  

def obtener_precio():
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    precio_elemento = soup.find("span", {"class": "andes-money-amount__fraction"})
    if precio_elemento:
        precio = int(precio_elemento.get_text().replace(".", ""))
        return precio
    return None

precio_actual = obtener_precio()

if precio_actual:
    print(f"💰 Precio actual: ${precio_actual}")
    if precio_actual <= precio_objetivo:
        print("🔥 ¡El precio bajó! Es hora de comprar 🚀")
    else:
        print("📉 Todavía no está en el precio que querés...")
else:
    print("❌ No se pudo obtener el precio. Puede que la estructura de la página haya cambiado.")
