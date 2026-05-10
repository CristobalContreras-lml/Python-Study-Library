# ============================================================
# FUNDAMENTOS DE PYTHON - Manejo de Excepciones
# ============================================================

# En Python, los errores que ocurren durante la ejecución de un programa
# se llaman "excepciones". En lugar de que el programa se caiga (crashee),
# podemos "atrapar" estos errores y manejarlos de forma controlada.

# ── 1. BLOQUE TRY - EXCEPT ───────────────────────────────────
# Ponemos el código que podría fallar dentro del bloque 'try'.
# Si falla, se ejecuta el bloque 'except'.

print("=== TRY / EXCEPT BÁSICO ===")
try:
    # Intentamos dividir por cero (lo cual dará error)
    resultado = 10 / 0
    print("El resultado es:", resultado)
except ZeroDivisionError:
    # Esto se ejecuta solo si ocurre el error específico de división por cero
    print("Error: ¡No se puede dividir entre cero!")

# ── 2. ATRAPAR DISTINTOS TIPOS DE ERRORES ────────────────────
# Puedes tener múltiples bloques except para manejar diferentes situaciones.

print("\n=== MÚLTIPLES EXCEPT ===")
try:
    numero_texto = "letras"
    # Convertir letras a entero generará un ValueError
    numero = int(numero_texto)
    division = 100 / numero
except ValueError:
    print("Error de valor: No introdujiste un número válido.")
except ZeroDivisionError:
    print("Error de división: El número introducido fue cero.")
except Exception as e:
    # Exception atrapa CUALQUIER otro error no especificado arriba.
    # 'as e' nos permite guardar el mensaje original del error en la variable 'e'.
    print("Ocurrió un error inesperado:", e)

# ── 3. BLOQUES ELSE Y FINALLY ────────────────────────────────
# - 'else': Se ejecuta SOLO si el bloque 'try' tuvo éxito (no hubo errores).
# - 'finally': Se ejecuta SIEMPRE, haya ocurrido un error o no.
#   (Se usa mucho para cerrar archivos, cerrar conexiones a bases de datos, etc.)

print("\n=== ELSE Y FINALLY ===")
try:
    calculo = 10 / 2
except Exception:
    print("Hubo un error")
else:
    print("El cálculo se realizó con éxito:", calculo)
finally:
    print("Este bloque 'finally' se ejecuta siempre al terminar.")


# ============================================================
# EJERCICIOS
# ============================================================
print("\n=== EJERCICIOS ===")

# Ejercicio 1: Escribe un bloque try-except para manejar el error 
# que ocurre al intentar acceder a un índice que no existe en la lista.
lista_frutas = ["Manzana", "Naranja", "Pera"]
# Tu código aquí:
# Intenta imprimir lista_frutas[5] y maneja el IndexError.



# Ejercicio 2: Tienes un diccionario con edades. Intenta acceder a la llave "Pedro" 
# e imprimirla. Usa try-except para manejar el error si la llave no existe (KeyError)
# e imprime un mensaje amigable como "Pedro no está en el diccionario".
edades = {"Juan": 25, "Ana": 30}
# Tu código aquí:



# Ejercicio 3: Pide al usuario que introduzca un número usando input() o simplemente 
# asigna un string a una variable (ej. entrada = "Hola"). Intenta convertir esa 
# variable a tipo float(). Usa try-except-else. Si falla, imprime "Entrada no válida". 
# Si tiene éxito (else), imprime "Conversión exitosa: " seguido del número.
# Tu código aquí:



# Ejercicio 4 (Avanzado): Crea una función llamada 'dividir_seguro(a, b)' que retorne
# el resultado de a / b. Usa try-except para atrapar ZeroDivisionError y TypeError 
# (si a o b no son números). Si hay error, la función debe retornar None y mostrar un mensaje.
# Tu código aquí:


