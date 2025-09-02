import math

funciones = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
funciones.update({"abs":abs, "round": round})

print(" Calculadora cientifica (escribi 'salir' para terminar)")

while True:
    expr = input(">>> ")
    if expr.lower() == "salir":
        break
    try:
        resultado = eval(expr, {"__builtins__": None}, funciones)
        print("= ", resultado)
    except Exception as e:
        print("Error: ", e)
