class Celular():
    
    #variables
    def __init__(self, marca,modelo,camera = "100MP"):
        self.marca = marca
        self.modelo = modelo
        self.camera = camera
    
    def __del__(self):
        #Los destructores son eliminar el objeto, y que realicen alguna accion o ejecuten un metodo antes se pueden utilizar este metodo
         print("Destroying object...")
        
print("Crear celulares")

Celular_lista = []
Celular_1 = Celular("sansung", "S23", "40PMX")
Celular_2 = Celular("sansung", "S13", "40PMX")

print("Agregar a la lista")
Celular_lista.append(Celular_1)
Celular_lista.append(Celular_2)

print(len(Celular_lista))



print("Borrar el celular 1")

#Forma 1 de desruir un objeto pero no se eliina de la lista ya que es none no esta eliminado de memoria en si
# Celular_lista[1] = None

# #Forma 2 de desturir una objeto
del Celular_lista[0]


del Celular_lista[0]

#Produce un error ya que celular_1 y celular_2 dejaron de existir

print(len(Celular_lista))