# ============================================================
# SOLUCIONES - Tuplas y Sets (Conjuntos)
# ============================================================

print("=== SOLUCIONES: TUPLAS Y SETS ===\n")

# Ejercicio 1: Crea una tupla llamada 'meses' con los primeros 4 meses del año. 
# Imprime el tercer mes.
print("--- Solución Ejercicio 1 ---")
meses = ("Enero", "Febrero", "Marzo", "Abril")
print("Tercer mes:", meses[2]) # Recuerda que los índices empiezan en 0
print()


# Ejercicio 2: Dada la siguiente lista de números con duplicados, 
# conviértela a un set para eliminar los duplicados y luego imprímela.
print("--- Solución Ejercicio 2 ---")
lista_numeros = [10, 20, 10, 30, 40, 20, 50]
numeros_sin_duplicados = set(lista_numeros)
print("Lista original:", lista_numeros)
print("Set sin duplicados:", numeros_sin_duplicados)
print()


# Ejercicio 3: Tienes dos listas de estudiantes inscritos en dos cursos diferentes.
# Encuentra y muestra a los estudiantes que están inscritos en AMBOS cursos.
print("--- Solución Ejercicio 3 ---")
curso_python = ["Ana", "Carlos", "Beatriz", "David"]
curso_datos = ["Beatriz", "Elena", "Carlos", "Fernando"]

# Convertimos las listas a sets y usamos intersección
set_python = set(curso_python)
set_datos = set(curso_datos)
estudiantes_en_ambos = set_python.intersection(set_datos)
# o también: estudiantes_en_ambos = set_python & set_datos

print("Estudiantes en ambos cursos:", estudiantes_en_ambos)
print()


# Ejercicio 4: Intenta desempaquetar la tupla 'dimensiones' en tres variables: 
# largo, ancho y alto. Luego imprímelas.
print("--- Solución Ejercicio 4 ---")
dimensiones = (100, 50, 25)

largo, ancho, alto = dimensiones

print(f"Largo: {largo}")
print(f"Ancho: {ancho}")
print(f"Alto: {alto}")
print()
