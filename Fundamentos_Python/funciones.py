
# ============================================================
# FUNDAMENTOS DE PYTHON - Funciones (def)
# ============================================================
# Una función es un bloque de código con nombre con el fin de reutilizarlo a futuro y que no se tan redundante

# ── 1. FUNCIÓN BÁSICA ────────────────────────────────────────

def greet_user():
    print("Hola! lml")
    
greet_user()


def greet_user(username):
    print(f"Saludos {username.title()}")
 
greet_user('cristobal')



def sumar(a,b):
    return a + b

resultado = sumar(6,4)

print(f"La suma de los dos parámetros es: \n{resultado}")


def tomar_cafe(tipo, tazasCantidad):
    print(f"Sirviendo {tazasCantidad} de {tipo} al cliente de la mesa X")
    
tomar_cafe("Capuchinno", 1)



def saludar():
    print("¡Hola! Bienvenido 👋")
 
saludar()   # así se llama (ejecuta) una función
 
 
# ── 2. FUNCIÓN CON PARÁMETROS ────────────────────────────────
# Los parámetros son datos que le pasas a la función
def saludar_a(nombre):
    print(f"¡Hola, {nombre}! 👋")
 
saludar_a("Cristóbal")
saludar_a("Python")
 
 
# ── 3. FUNCIÓN CON RETURN ────────────────────────────────────
# return devuelve un resultado para usarlo después
def sumar(a, b):
    return a + b
 
resultado = sumar(10, 5)
print("10 + 5 =", resultado)
 
 
# ── 4. PARÁMETROS CON VALOR POR DEFECTO ──────────────────────
# Si no pasas el argumento, usa el valor por defecto
def potencia(base, exponente=2):    # por defecto eleva al cuadrado
    return base ** exponente
 
print("3 al cuadrado:", potencia(3))       # usa exponente=2
print("3 al cubo:    ", potencia(3, 3))    # usa exponente=3
 
 
# ── 5. MÚLTIPLES RETURN ──────────────────────────────────────
def clasificar_nota(nota):
    if nota >= 90:
        return "Sobresaliente 🏆"
    elif nota >= 60:
        return "Aprobado ✔"
    else:
        return "Reprobado ✗"
 
print(clasificar_nota(95))
print(clasificar_nota(72))
print(clasificar_nota(40))
 
 
# ── 6. FUNCIÓN QUE RETORNA VARIOS VALORES ────────────────────
def min_max(lista):
    return min(lista), max(lista)   # retorna una tupla
 
minimo, maximo = min_max([4, 8, 1, 9, 3])
print(f"Mínimo: {minimo} | Máximo: {maximo}")
 
 
# ── 7. EJEMPLO FINAL — Calculadora ───────────────────────────
def calcular(a, b, operacion="suma"):
    if operacion == "suma":        return a + b
    elif operacion == "resta":     return a - b
    elif operacion == "producto":  return a * b
    elif operacion == "division":  return a / b if b != 0 else "Error: división por cero"
 
print(calcular(10, 5))                      # suma por defecto
print(calcular(10, 5, "resta"))
print(calcular(10, 5, "producto"))
print(calcular(10, 0, "division"))