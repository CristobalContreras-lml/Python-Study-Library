# ============================================================
# FUNDAMENTOS DE PYTHON - Bucles (for / while)
# ============================================================
# Los bucles sirven para repetir instrucciones automáticamente
# sin tener que escribir lo mismo muchas veces.


# ── 1. BUCLE FOR ─────────────────────────────────────────────
# Ideal cuando sabes cuántas veces quieres repetir algo.

print("=== FOR básico: contar del 1 al 5 ===")
for numero in range(1, 6):   # range(inicio, fin) → el fin NO se incluye
    print(numero)

print("\n=== FOR: contar de 2 en 2 ===")
for numero in range(0, 11, 2):   # range(inicio, fin, paso)
    print(numero, end=" ")       # end=" " imprime en la misma línea
print()  # salto de línea al terminar

print("\n=== FOR: recorrer una lista ===")
frutas = ["manzana", "banana", "cereza", "mango"]
for fruta in frutas:
    print("Fruta:", fruta)

print("\n=== FOR con enumerate() ===")
# enumerate() te da el índice Y el valor al mismo tiempo
for indice, fruta in enumerate(frutas):
    print(f"  [{indice}] {fruta}")

print("\n=== FOR: recorrer un string letra por letra ===")
palabra = "Python"
for letra in palabra:
    print(letra, end="-")
print()


# ── 2. BUCLE WHILE ───────────────────────────────────────────
# Ideal cuando no sabes cuántas veces se va a repetir,
# sino que depende de una condición.

print("\n=== WHILE básico ===")
contador = 1
while contador <= 5:
    print("Vuelta número:", contador)
    contador += 1      # ⚠️ IMPORTANTE: siempre avanza, si no → bucle infinito

print("\n=== WHILE: adivina el número ===")
# Simulamos que el usuario tiene que adivinar (sin input real)
numero_secreto = 7
intento = 1
intentos_del_usuario = [3, 5, 7]   # simulamos respuestas del usuario

for respuesta in intentos_del_usuario:
    if respuesta == numero_secreto:
        print(f"Intento {intento}: ¡Correcto! El número era {numero_secreto} 🎉")
        break
    else:
        print(f"Intento {intento}: {respuesta} es incorrecto. Intenta de nuevo.")
    intento += 1


# ── 3. BREAK Y CONTINUE ──────────────────────────────────────
print("\n=== BREAK: salir del bucle antes de tiempo ===")
for numero in range(1, 10):
    if numero == 5:
        print("  ¡Llegué al 5! Me detengo aquí.")
        break          # sale del bucle inmediatamente
    print(" ", numero)

print("\n=== CONTINUE: saltar una vuelta específica ===")
print("Números del 1 al 8, saltando el 4 y el 6:")
for numero in range(1, 9):
    if numero == 4 or numero == 6:
        continue       # salta esta vuelta y sigue con la siguiente
    print(" ", numero, end=" ")
print()


# ── 4. FOR CON ELSE ──────────────────────────────────────────
# El bloque else de un for se ejecuta SOLO si el bucle
# terminó sin un break. ¡Poco conocido pero muy útil!
print("\n=== FOR con ELSE ===")
numeros = [2, 4, 6, 8, 10]

for n in numeros:
    if n % 2 != 0:      # si encuentra un impar
        print("Se encontró un número impar:", n)
        break
else:
    print("Todos los números son pares ✔")


# ── 5. BUCLES ANIDADOS ───────────────────────────────────────
print("\n=== Tablas de multiplicar (2 y 3) ===")
for tabla in [2, 3]:
    print(f"\n  --- Tabla del {tabla} ---")
    for i in range(1, 6):
        print(f"  {tabla} x {i} = {tabla * i}")
