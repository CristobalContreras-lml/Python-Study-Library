# " CLASES "

# class Dog:
#      """ Un intento sencillo para modelar un perro"""
#      def __init__(self, name, age):
#          self.name = name
#          self.age= age
    
#      def sit(self):
#          """ Simula sentarse ante una orden"""
#          print(f"{self.name} is now sitting")
        
#      def laPatita(self):
#          "El perro será cordial"
#          print(f"{self.name} entrega la patita!:O")
         
         
# my_dog = Dog("Manchitas",10)

# print(f"My dog name is {my_dog.name}")
# print(f"My dog is {my_dog.age} old")

# """ Uso de funciones de Dog"""
               
# my_dog.sit()        
# my_dog.laPatita()

# your_dog= Dog("Patitas",7)

# print("Hay otro perro que se acerca en el parque")
# print("Cómo se llama tu perro?")
# print(f"Se llama {your_dog.name} y tiene {your_dog.age} años")

# your_dog.sit()
# your_dog.laPatita()

# """ Otro ejemplo"""

# class Usuario:
#     def __init__(self, nombre, apellido):
#         self.nombre= nombre
#         self.apellido= apellido
    
#     def describir_usuario(self):
#         print(f"El usuario {self.nombre} trabaja para empresa X, Sucursal 1")
        
#     def saludar_usuario(self):
#         print(f"Bienvenido {self.nombre} {self.apellido}!:)")

# us1= Usuario("Cristobal","Contreras")
# us1.saludar_usuario()
# us1.describir_usuario()

# class CuentaBancaria:
#     def __init__(self, titular, saldo_inicial):
#         self.titular = titular
#         self.saldo = saldo_inicial

#     def depositar(self, cantidad):
#         self.saldo += cantidad
#         return f"Depósito exitoso. Nuevo saldo: ${self.saldo}"

#     def retirar(self, cantidad):
#         if cantidad <= self.saldo:
#             self.saldo -= cantidad
#             return f"Retiro exitoso. Saldo restante: ${self.saldo}"
#         else:
#             return "Fondos insuficientes."

# # --- Uso de la clase ---

# # Creamos la cuenta de "Ana" con 100 dólares
# mi_cuenta = CuentaBancaria("Ana", 100)

# print(mi_cuenta.depositar(50))  # Salida: Nuevo saldo: $150
# print(mi_cuenta.retirar(30))    # Salida: Saldo restante: $120
# print(mi_cuenta.retirar(200))   # Salida: Fondos insuficientes.




# class Administrador(Usuario):
#     """ Un tipo en especial de usuario con privilegios"""
    
#     def __init__(self, nombre, apellido):
#         super().__init__(nombre, apellido)
#         self.privilegios = ["Puede borrar post", "Puede borrar Usuarios", "Puede modificar archivos"]
    
#     def mostrar_privilegios(self):
#         """Muestra lo que el Admin es capaz de hacer"""
#         print(f"El administrador {self.nombre} tiene los siguientes permisos:\n")
#         for permiso in self.privilegios:
#             print(f"- {permiso}")
            
# admin_01= Administrador("Cristobal", "Admin")   
# admin_01.saludar_usuario()
# admin_01.mostrar_privilegios() 



from random import choice

players = ["cris", "moni", "camilo", "manuel", "martin", "estefania"]
first_up = choice(players)
print(f"El primer jugador en salir es: {first_up}")

from random import randint
print(f"El número es {randint(1, 12)}")

class Dado:
    def __init__(self, caras= 6):
        self.caras = caras
        
    def tirar_dado(self):
        resultado = randint (1, self.caras)
        print(f"Lanzamiento: {resultado}")
 
 
print("-------Lanzando dados con 6 caras , 10 veces------\n")
dado_6 = Dado ()
for _ in range (10):
    dado_6.tirar_dado()

print("\n")

print("-------Lanzando dados con 10 caras , 10 veces------\n")
dado_10 = Dado(10)
for _ in range (10):
    dado_10.tirar_dado()

print("\n")

print("-------Lanzando dados con 20 caras , 10 veces------\n")    
dado_20 = Dado(20)   
for _ in range (10):
    dado_20.tirar_dado()
    
print("\n")
    

       