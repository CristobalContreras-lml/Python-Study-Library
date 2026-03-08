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