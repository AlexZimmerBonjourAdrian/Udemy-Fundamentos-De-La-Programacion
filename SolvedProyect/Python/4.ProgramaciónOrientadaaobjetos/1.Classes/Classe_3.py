#nombre de clase en el editor y nombre de la clase en el archivo
from Classe_2 import class_2
from Classe_4 import class_4


class class_3():
    def __init__(self, Nombre):
        self.Nombre = Nombre
    
    def NombreClase(self):
        print("Esta es la clase_3")
    
    def classNombre(self):
        clase_2 = class_2("foo")
        clase_4 = class_4("foo")
        clase_2.NombreClase()
        clase_4.NombreClase()

clase = class_3("foo")

clase.NombreClase()

print(" ")
clase.classNombre()