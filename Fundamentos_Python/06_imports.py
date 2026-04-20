# """ Las siguientes funciones presentadas son de la Biblioteca misma de Python llamada random """

# """ La funcion choice es una eleccion impredecible de un numero"""

# from random import choice

# players = ["cris", "moni", "camilo", "manuel", "martin", "estefania"]

# first_up = choice(players)

# print(f"El primer jugador en salir es: {first_up}")

# """ La funcion randint es para elegir numeros aleatorios de incio-fin"""

# from random import randint

# print(f"El número es {randint(1, 12)}")

# class Dado:
#     def __init__(self, caras= 6):
#         self.caras = caras
        
#     def tirar_dado(self):
#         resultado = randint (1, self.caras)
#         print(f"Lanzamiento: {resultado}")
 
 
# print("-------Lanzando dados con 6 caras , 10 veces------\n")
# dado_6 = Dado ()
# for _ in range (10):
#     dado_6.tirar_dado()

# print("\n")

# print("-------Lanzando dados con 10 caras , 10 veces------\n")
# dado_10 = Dado(10)
# for _ in range (10):
#     dado_10.tirar_dado()

# print("\n")

# print("-------Lanzando dados con 20 caras , 10 veces------\n")    
# dado_20 = Dado(20)   
# for _ in range (10):
#     dado_20.tirar_dado()
    
# print("\n")
    
    
# # otro ejemplo de choice
# # Lotería

# tómbola= [6,8,4,2,1,7,0,9,4,5,"a","b","u","r","s"]

# boleto_win = []

# for i in range (4):
#     seleccionado = choice(tómbola)
#     boleto_win.append(seleccionado)

# print(f"Estos números o letras son los ganadores!!: {boleto_win}\n")


# ---sample hace que escoga valores de forma aletoria e irrepetible los valores-------

from random import sample

opciones = ["1","2","3","4","5","6","7","8","9","0","A","B","C","D"]

mi_boleto = ["7","4","D","C"]

intentos = 0

while True:
    intentos +=1
    ticket_ganador = sample(opciones,4)
    
    if sorted(ticket_ganador) == sorted(mi_boleto):
        break

print(f"El ticket ganador es {ticket_ganador}")
print(f"la cantidad de veces que tuve que jugar con mi boleto: {mi_boleto} , fue una cantidad de {intentos}")
