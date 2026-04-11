# ============================================================
# FUNDAMENTOS DE PYTHON - Listas y Diccionarios
# ============================================================


# ╔══════════════════════════════════════════════════════════╗
# ║                        LISTAS                           ║
# ╚══════════════════════════════════════════════════════════╝
# Una lista guarda varios valores EN ORDEN dentro de [ ]
# Puede mezclar tipos, pero en la práctica se usa un solo tipo.

print("=" * 45)
print("                   LISTAS")
print("=" * 45)

# ── Crear una lista ──────────────────────────────────────────
frutas    = ["manzana", "banana", "cereza", "mango"]
numeros   = [10, 20, 30, 40, 50]
mezclada  = [1, "hola", True, 3.14]

print("\nLista de frutas:", frutas)
print("Lista de números:", numeros)


# ── Acceder a elementos (índice) ─────────────────────────────
# Los índices empiezan en 0
print("\n--- Acceso por índice ---")
print("Primera fruta  (índice  0):", frutas[0])   # manzana
print("Tercera fruta  (índice  2):", frutas[2])   # cereza
print("Última fruta   (índice -1):", frutas[-1])  # mango  ← índice negativo


# ── Rebanadas / Slicing ──────────────────────────────────────
print("\n--- Slicing lista[inicio:fin] ---")
print("Primeras 2 frutas:", frutas[0:2])    # ['manzana', 'banana']
print("Desde la 2da:     ", frutas[1:])     # desde índice 1 hasta el final
print("Últimas 2:        ", frutas[-2:])    # las 2 últimas


# ── Modificar una lista ──────────────────────────────────────
print("\n--- Modificar ---")
frutas.append("uva")          # agrega al final
print("Después de append():", frutas)

frutas.insert(1, "kiwi")      # inserta en la posición 1
print("Después de insert():", frutas)

frutas.remove("banana")       # elimina por valor
print("Después de remove():", frutas)

eliminado = frutas.pop()      # elimina y devuelve el último elemento
print(f"pop() eliminó '{eliminado}'. Lista:", frutas)

frutas[0] = "pera"            # reemplaza el elemento en índice 0
print("Después de reemplazar índice 0:", frutas)


# ── Métodos útiles ───────────────────────────────────────────
print("\n--- Métodos útiles ---")
numeros_desordenados = [34, 1, 89, 12, 55]
print("Lista original:        ", numeros_desordenados)

numeros_desordenados.sort()
print("Después de sort():     ", numeros_desordenados)

numeros_desordenados.reverse()
print("Después de reverse():  ", numeros_desordenados)

print("Longitud con len():    ", len(numeros_desordenados))
print("¿Está el 89?:          ", 89 in numeros_desordenados)  # True
print("Suma de elementos:     ", sum(numeros_desordenados))
print("Máximo:                ", max(numeros_desordenados))
print("Mínimo:                ", min(numeros_desordenados))


# ── Recorrer una lista ───────────────────────────────────────
print("\n--- Recorrer con for ---")
colores = ["rojo", "verde", "azul"]
for color in colores:
    print(f"  Color: {color}")


# ╔══════════════════════════════════════════════════════════╗
# ║                     DICCIONARIOS                        ║
# ╚══════════════════════════════════════════════════════════╝
# Un diccionario guarda pares CLAVE: VALOR dentro de { }
# Perfecto para representar objetos o registros.

print("\n" + "=" * 45)
print("                DICCIONARIOS")
print("=" * 45)


# ── Crear un diccionario ─────────────────────────────────────
persona = {
    "nombre": "Carlos",
    "edad": 28,
    "ciudad": "Santiago",
    "activo": True
}
print("\nDiccionario persona:", persona)


# ── Acceder a valores ────────────────────────────────────────
print("\n--- Acceso por clave ---")
print("Nombre:", persona["nombre"])
print("Edad:  ", persona["edad"])

# .get() es más seguro: no da error si la clave no existe
print("País:  ", persona.get("pais", "No especificado"))  # valor por defecto


# ── Modificar un diccionario ─────────────────────────────────
print("\n--- Modificar ---")
persona["email"] = "carlos@email.com"   # agregar nueva clave
persona["edad"]  = 29                   # actualizar valor existente
print("Después de agregar email y cambiar edad:", persona)

del persona["activo"]                   # eliminar una clave
print("Después de del 'activo':", persona)


# ── Métodos útiles ───────────────────────────────────────────
print("\n--- Métodos útiles ---")
print("Claves   (.keys()):  ", list(persona.keys()))
print("Valores  (.values()):", list(persona.values()))
print("Pares    (.items()): ", list(persona.items()))
print("¿Existe 'nombre'?:   ", "nombre" in persona)   # True
print("¿Existe 'telefono'?: ", "telefono" in persona)  # False


# ── Recorrer un diccionario ──────────────────────────────────
print("\n--- Recorrer con for ---")
for clave, valor in persona.items():
    print(f"  {clave}: {valor}")


# ── Lista de diccionarios (muy común en la vida real) ────────
print("\n--- Lista de diccionarios ---")
estudiantes = [
    {"nombre": "Ana",    "nota": 95},
    {"nombre": "Luis",   "nota": 82},
    {"nombre": "María",  "nota": 90},
]

for est in estudiantes:
    estado = "Aprobado ✔" if est["nota"] >= 85 else "En proceso ✗"
    print(f"  {est['nombre']}: {est['nota']} → {estado}")


# ── Diccionario anidado ──────────────────────────────────────
print("\n--- Diccionario anidado ---")
empresa = {
    "nombre": "Tech Corp",
    "direccion": {
        "calle": "Av. Providencia 100",
        "ciudad": "Santiago",
        "pais": "Chile"
    },
    "empleados": 150
}

print("Empresa:", empresa["nombre"])
print("Ciudad: ", empresa["direccion"]["ciudad"])  # acceso anidado
print("País:   ", empresa["direccion"]["pais"])
