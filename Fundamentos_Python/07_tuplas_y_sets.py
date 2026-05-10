# ============================================================
# FUNDAMENTOS DE PYTHON - Tuplas y Sets (Conjuntos)
# ============================================================

# ── 1. TUPLAS ────────────────────────────────────────────────
# Las tuplas son como las listas, pero son INMUTABLES.
# Una vez creadas, no se pueden modificar, añadir o eliminar elementos.
# Se definen usando paréntesis ().

coordenadas = (10.5, 20.3)
colores_rgb = ("Rojo", "Verde", "Azul")
un_solo_elemento = ("Hola",) # Requiere coma para ser tupla, si no es solo un string en paréntesis

print("=== TUPLAS ===")
print("Coordenadas:", coordenadas)
print("Color en índice 1:", colores_rgb[1])
print("Tipo:", type(coordenadas))

# Desempaquetado de tuplas (Tuple unpacking)
x, y = coordenadas
print(f"X: {x}, Y: {y}")

# Las tuplas son útiles para datos que no deben cambiar o para retornar múltiples valores en una función.
# Intentar hacer: coordenadas[0] = 15.0 generará un TypeError.


# ── 2. SETS (CONJUNTOS) ──────────────────────────────────────
# Los sets son colecciones desordenadas de elementos ÚNICOS.
# No permiten duplicados y no tienen índice (no puedes hacer mi_set[0]).
# Se definen usando llaves {}.

numeros_unicos = {1, 2, 3, 3, 4, 4, 5}
nombres = {"Ana", "Juan", "Pedro", "Ana"}

print("\n=== SETS ===")
print("Números únicos:", numeros_unicos) # Nota que los duplicados desaparecen
print("Nombres:", nombres)
print("Tipo:", type(numeros_unicos))

# Añadir y remover elementos
frutas = {"Manzana", "Pera"}
frutas.add("Banana")
frutas.remove("Pera")
print("Frutas actualizadas:", frutas)

# Operaciones de conjuntos matemáticos
grupo_a = {"Ana", "Juan", "Maria"}
grupo_b = {"Juan", "Pedro", "Maria", "Luis"}

print("\n--- Operaciones de Conjuntos ---")
print("Intersección (están en ambos):", grupo_a.intersection(grupo_b))
print("Unión (todos, sin repetir):", grupo_a.union(grupo_b))
print("Diferencia (en A pero no en B):", grupo_a.difference(grupo_b))

# ============================================================
# EJERCICIOS
# ============================================================
print("\n=== EJERCICIOS ===")

# Ejercicio 1: Crea una tupla llamada 'meses' con los primeros 4 meses del año. 
# Imprime el tercer mes.


# Ejercicio 2: Dada la siguiente lista de números con duplicados, 
# conviértela a un set para eliminar los duplicados y luego imprímela.
lista_numeros = [10, 20, 10, 30, 40, 20, 50]
# Tu código aquí:


# Ejercicio 3: Tienes dos listas de estudiantes inscritos en dos cursos diferentes.
# Encuentra y muestra a los estudiantes que están inscritos en AMBOS cursos.
curso_python = ["Ana", "Carlos", "Beatriz", "David"]
curso_datos = ["Beatriz", "Elena", "Carlos", "Fernando"]
# Tu código aquí:


# Ejercicio 4: Intenta desempaquetar la tupla 'dimensiones' en tres variables: 
# largo, ancho y alto. Luego imprímelas.
dimensiones = (100, 50, 25)
# Tu código aquí:

