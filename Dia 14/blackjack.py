import random
import os
import time

# --- Utilidades ---
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def valor_mano(mano):
    # Suma cartas tratando As como 1 o 11
    total = 0
    ases = 0
    for c in mano:
        if c in ["J","Q","K"]:
            total += 10
        elif c == "A":
            ases += 1
            total += 1  # contarlos primero como 1
        else:
            total += int(c)
    # intentar convertir algunos Ases a 11 si no pasa de 21
    for _ in range(ases):
        if total + 10 <= 21:
            total += 10
    return total

def mostrar_manos(jugador, dealer, ocultar_dealer=True):
    if ocultar_dealer:
        print(f"Dealer: [ {dealer[0]} , ? ]")
    else:
        print(f"Dealer: {dealer} -> {valor_mano(dealer)}")
    print(f"Tú:     {jugador} -> {valor_mano(jugador)}")

# --- Baraja ---
def crear_baraja():
    valores = [str(n) for n in range(2,11)] + ["J","Q","K","A"]
    palos = ["♠","♥","♦","♣"]
    baraja = [v for v in valores for _ in palos]  # solo importa el valor
    random.shuffle(baraja)
    return baraja

# --- Juego ---
def jugar_mano():
    baraja = crear_baraja()
    jugador = [baraja.pop(), baraja.pop()]
    dealer = [baraja.pop(), baraja.pop()]

    # Turno jugador
    while True:
        clear()
        print("=== Blackjack ===\n")
        mostrar_manos(jugador, dealer, ocultar_dealer=True)

        v_j = valor_mano(jugador)
        if v_j == 21:
            print("\nBLACKJACK! Revisando dealer...")
            break
        if v_j > 21:
            print("\nTe pasaste! (Bust)")
            return "dealer", jugador, dealer

        accion = input("\n¿Pedir (p) o Plantarse (s)? ").strip().lower()
        if accion in ["p","pedir","hit"]:
            jugador.append(baraja.pop())
            continue
        elif accion in ["s","plantarse","stand"]:
            break
        else:
            print("Opción inválida. Usá 'p' o 's'.")
            time.sleep(0.8)

    # Turno dealer (revela)
    clear()
    print("=== Blackjack ===\n")
    mostrar_manos(jugador, dealer, ocultar_dealer=False)
    time.sleep(1)

    while valor_mano(dealer) < 17:
        print("\nDealer pide...")
        dealer.append(baraja.pop())
        mostrar_manos(jugador, dealer, ocultar_dealer=False)
        time.sleep(1)

    v_j = valor_mano(jugador)
    v_d = valor_mano(dealer)

    if v_d > 21:
        print("\nDealer se pasó. Ganaste!")
        return "jugador", jugador, dealer
    if v_j > v_d:
        print("\nGanaste!")
        return "jugador", jugador, dealer
    if v_j < v_d:
        print("\nPerdiste.")
        return "dealer", jugador, dealer
    print("\nEmpate (Push).")
    return "push", jugador, dealer

def main():
    clear()
    print("===== Blackjack (consola) — Día 14 =====\n")
    banca = 1000
    while True:
        print(f"Banca: ${banca}")
        try:
            apuesta = int(input("Apuesta (0 para salir): $"))
        except ValueError:
            print("Ingresa un número válido.")
            continue
        if apuesta == 0:
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        if apuesta < 0 or apuesta > banca:
            print("Apuesta inválida.")
            continue

        resultado, jugador, dealer = jugar_mano()
        if resultado == "jugador":
            # blackjack natural paga 1.5 si jugador tiene 21 con 2 cartas
            if valor_mano(jugador) == 21 and len(jugador) == 2:
                pago = int(apuesta * 1.5)
                banca += pago
                print(f"Blackjack! Cobrás ${pago}.")
            else:
                banca += apuesta
                print(f"Ganáste ${apuesta}.")
        elif resultado == "dealer":
            banca -= apuesta
            print(f"Perdíste ${apuesta}.")
        else:
            print("Apuesta devuelta (empate).")

        if banca <= 0:
            print("Te quedaste sin dinero. Juego terminado.")
            break

        input("\nEnter para continuar...")
        clear()

if __name__ == "__main__":
    main()
