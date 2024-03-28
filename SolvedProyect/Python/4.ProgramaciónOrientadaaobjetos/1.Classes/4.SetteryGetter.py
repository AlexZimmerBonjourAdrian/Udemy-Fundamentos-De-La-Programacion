#Setter y Getter


class auto:
    #Consturctor de celular
        def __init__(self, marca, modelo):
            self.marca = marca
            self.modelo = modelo
               
        def getMarca(self):
            return self.marca 
        
        def setMarca(self,Marca):
            self.marca = Marca

        def setMarca(self,Modelo):
             self.modelo = Modelo
        
        def getMarca():
             return self.modelo   
         
        def __del__(self):
        #Los destructores son eliminar el objeto, y que realicen alguna accion o ejecuten un metodo antes se pueden utilizar este metodo
         print("Destroying object...")
        
print("Se crea el auto")   
auto_1 = auto("bolt","13B")   

print("Muestra su variable original")   
print(auto_1.getMarca())

print("Set nuevo valor de marca")      
auto_1.setMarca("fusquito")

print("Imprime marca denuevo")      
print(auto_1.getMarca())

