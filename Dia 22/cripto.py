import requests
import time

# https://github.com/lucmadev/30-Dias-de-Python

API_URL = "https://api.binance.com/api/v3/ticker/price"

def get_price(symbol):
    try:
        response = requests.get(API_URL, params={"symbol": symbol})
        data = response.json()
        return float(data["price"])
    except Exception as e:
        print(f"Error obteniendo {symbol}: {e}")
        return None

def compare_cryptos(symbols):
    print("=== Comparador de Criptos (Binance) ===\n")
    while True:
        for sym in symbols:
            price = get_price(sym)
            if price:
                print(f"{sym}: {price} USDT")
        print("-" * 40)
        time.sleep(1)

if __name__ == "__main__":
    cryptos = ["BTCUSDT", "ETHUSDT", "XRPUSDT"]
    compare_cryptos(cryptos)
