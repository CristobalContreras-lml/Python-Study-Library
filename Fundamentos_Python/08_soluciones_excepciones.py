# ============================================================
# SOLUCIONES - Manejo de Excepciones
# ============================================================

print("=== SOLUCIONES: MANEJO DE EXCEPCIONES ===\n")

# Ejercicio 1: Escribe un bloque try-except para manejar el error 
# que ocurre al intentar acceder a un índice que no existe en la lista.
print("--- Solución Ejercicio 1 ---")
lista_frutas = ["Manzana", "Naranja", "Pera"]
try:
    # Esto generará un IndexError
    print(lista_frutas[5])
except IndexError:
    print("Error: Ese índice no existe en la lista.")
print()


# Ejercicio 2: Tienes un diccionario con edades. Intenta acceder a la llave "Pedro" 
# e imprimirla. Usa try-except para manejar el error si la llave no existe (KeyError)
# e imprime un mensaje amigable como "Pedro no está en el diccionario".
print("--- Solución Ejercicio 2 ---")
edades = {"Juan": 25, "Ana": 30}
try:
    edad_pedro = edades["Pedro"]
    print(edad_pedro)
except KeyError:
    print("Pedro no está en el diccionario de edades.")
print()


# Ejercicio 3: Intenta convertir una entrada a float(). Usa try-except-else.
print("--- Solución Ejercicio 3 ---")
entrada = "Hola"  # Puedes cambiar esto a "15.5" para probar el éxito
try:
    numero_convertido = float(entrada)
except ValueError:
    print("Entrada no válida: No se pudo convertir a número.")
else:
    print("Conversión exitosa:", numero_convertido)
print()


# Ejercicio 4 (Avanzado): Crea una función llamada 'dividir_seguro(a, b)'.
print("--- Solución Ejercicio 4 ---")
def dividir_seguro(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No puedes dividir por cero.")
        return None
    except TypeError:
        print("Error: Ambos valores deben ser números.")
        return None
    else:
        return resultado

# Probando la función:
print("Prueba 10 / 2:", dividir_seguro(10, 2))
print("Prueba 10 / 0:")
dividir_seguro(10, 0)
print("Prueba 10 / 'dos':")
dividir_seguro(10, "dos")
print()
