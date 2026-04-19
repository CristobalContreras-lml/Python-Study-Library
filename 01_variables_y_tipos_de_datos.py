# ============================================================
# FUNDAMENTOS DE PYTHON - Variables y Tipos de Datos
# ============================================================


# ── 1. NÚMEROS ENTEROS (int) ─────────────────────────────────
edad = 25
anio = 2024
temperatura_negativa = -10

print("=== ENTEROS ===")
print("Edad:", edad)
print("Año:", anio)
print("Temperatura negativa:", temperatura_negativa)
print("Tipo:", type(edad))  # <class 'int'>


# ── 2. NÚMEROS DECIMALES (float) ─────────────────────────────
precio = 19.99
pi = 3.14159
peso = 72.5

print("\n=== DECIMALES ===")
print("Precio:", precio)
print("Pi:", pi)
print("Tipo:", type(pi))  # <class 'float'>


# ── 3. CADENAS DE TEXTO (str) ────────────────────────────────
nombre = "Ana"
apellido = 'García'
mensaje = "¡Hola, mundo!"

print("\n=== TEXTO (str) ===")
print("Nombre:", nombre)
print("Apellido:", apellido)
print("Mensaje:", mensaje)
print("Tipo:", type(nombre))  # <class 'str'>

# Operaciones útiles con strings
print("Mayúsculas:", nombre.upper())
print("Longitud del nombre:", len(nombre))
print("Nombre + Apellido:", nombre + " " + apellido)

# F-strings: la forma moderna de combinar texto con variables
presentacion = f"Me llamo {nombre} {apellido} y tengo {edad} años."
print("F-string:", presentacion)


# ── 4. BOOLEANOS (bool) ──────────────────────────────────────
es_estudiante = True
tiene_trabajo  = False

print("\n=== BOOLEANOS ===")
print("¿Es estudiante?", es_estudiante)
print("¿Tiene trabajo?", tiene_trabajo)
print("Tipo:", type(es_estudiante))  # <class 'bool'>


# ── 5. CONVERSIÓN ENTRE TIPOS ────────────────────────────────
# A veces necesitas convertir un tipo a otro
print("\n=== CONVERSIÓN DE TIPOS ===")

numero_texto = "42"          # Esto es un string, NO un número
numero_real  = int(numero_texto)   # Lo convertimos a entero
print("Texto '42' convertido a entero:", numero_real)
print("Tipo antes:", type(numero_texto), "→ Tipo después:", type(numero_real))

decimal = 9.87
entero  = int(decimal)       # Convierte float a int (recorta decimales)
print(f"\nFloat {decimal} convertido a int: {entero}")

numero = 100
texto  = str(numero)         # Convierte número a texto
print(f"\nEntero {numero} convertido a str: '{texto}'")


# ── 6. COMPROBANDO EL TIPO DE UNA VARIABLE ──────────────────
print("\n=== isinstance() ===")
print("¿'edad' es un entero?  ", isinstance(edad, int))    # True
print("¿'precio' es un int?   ", isinstance(precio, int))  # False
print("¿'nombre' es un str?   ", isinstance(nombre, str))  # True
