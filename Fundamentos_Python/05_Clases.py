" CLASES "

class Dog:
     """ Un intento sencillo para modelar un perro"""
     def __init__(self, name, age):
         self.name = name
         self.age= age
    
     def sit(self):
         """ Simula sentarse ante una orden"""
         print(f"{self.name} is now sitting")
        
     def laPatita(self):
         "El perro será cordial"
         print(f"{self.name} entrega la patita!:O")
         
         
my_dog = Dog("Manchitas",10)

print(f"My dog name is {my_dog.name}")
print(f"My dog is {my_dog.age} old")

""" Uso de funciones de Dog"""
               
my_dog.sit()        
my_dog.laPatita()

your_dog= Dog("Patitas",7)

print("Hay otro perro que se acerca en el parque")
print("Cómo se llama tu perro?")
print(f"Se llama {your_dog.name} y tiene {your_dog.age} años")

your_dog.sit()
your_dog.laPatita()

""" Otro ejemplo"""

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre= nombre
        self.apellido= apellido
    
    def describir_usuario(self):
        print(f"El usuario {self.nombre} trabaja para empresa X, Sucursal 1")
        
    def saludar_usuario(self):
        print(f"Bienvenido {self.nombre} {self.apellido}!:)")

us1= Usuario("Cristobal","Contreras")
us1.saludar_usuario()
us1.describir_usuario()
        