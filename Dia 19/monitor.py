
# https://github.com/lucmadev/30-Dias-de-Python


import ipaddress
import platform
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
import socket
import csv
import argparse
from datetime import datetime

def ping(host: str, timeout_ms: int = 1000) -> bool:
    """
    Ping simple, cross-platform.
    Devuelve True si responde.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    # timeout param difiere: Windows uses -w (ms), Unix uses -W (seconds)
    if platform.system().lower() == "windows":
        cmd = ["ping", param, "1", "-w", str(timeout_ms), host]
    else:
        # convertir ms -> segundos (int ceil a 1s mínimo)
        timeout_s = max(1, int((timeout_ms + 999) // 1000))
        cmd = ["ping", param, "1", "-W", str(timeout_s), host]
    try:
        res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return res.returncode == 0
    except Exception:
        return False

def resolve_name(ip: str) -> str:
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return ""

def escanear_subred(cidr: str, workers: int = 100, timeout_ms: int = 1000):
    net = ipaddress.ip_network(cidr, strict=False)
    hosts = [str(h) for h in net.hosts()]
    activos = []

    print(f"Escaneando {len(hosts)} hosts en {cidr} ... (workers={workers})\n")
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(ping, ip, timeout_ms): ip for ip in hosts}
        for f in as_completed(futures):
            ip = futures[f]
            try:
                alive = f.result()
            except Exception:
                alive = False
            if alive:
                hostname = resolve_name(ip)
                activos.append((ip, hostname))
                print(f"✅ {ip}  {'- ' + hostname if hostname else ''}")
    print(f"\nEncontrados {len(activos)} hosts activos.")
    return activos

def guardar_csv(lista, path="hosts_activos.csv"):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ip","hostname","scan_timestamp"])
        ts = datetime.now().isoformat(timespec="seconds")
        for ip, host in lista:
            writer.writerow([ip, host, ts])
    print(f"📁 Guardado en {path}")

def main():
    parser = argparse.ArgumentParser(description="Escáner LAN (ping sweep) - Día 19")
    parser.add_argument("--cidr", default="192.168.1.0/24", help="Subred a escanear (ej: 192.168.1.0/24)")
    parser.add_argument("--workers", type=int, default=100, help="Hilos paralelos")
    parser.add_argument("--timeout", type=int, default=1000, help="Timeout ping en ms")
    parser.add_argument("--csv", action="store_true", help="Guardar resultados en CSV")
    args = parser.parse_args()

    activos = escanear_subred(args.cidr, workers=args.workers, timeout_ms=args.timeout)
    if args.csv and activos:
        guardar_csv(activos)

if __name__ == "__main__":
    main()
