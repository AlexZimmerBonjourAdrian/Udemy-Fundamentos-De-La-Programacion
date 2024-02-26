class Celular():
    
    #variables
    def __init__(self, marca,modelo,camera = "100MP"):
        self.marca = marca
        self.modelo = modelo
        self.camera = camera
     

        #metodos setter y getter

    def SetMarca(self, Marca):
            self.marca = Marca
        
    def GetMarca(self):
            return self.marca

        
    def SetModelo (self, Modelo):
            self.modelo = Modelo
        
    def GetModelo(self):
            return self.modelo


        
    def SetCamera(self, Camera):
            self.camera = Camera
        
    def GetCamera(self):
            return self.camera


        

    def __del__(self):
        #Los destructores son eliminar el objeto, y que realicen alguna accion o ejecuten un metodo antes se pueden utilizar este metodo
         print("Destroying object...")


celular_1 = Celular("sansung", "S13", "40PMX")
    
print(celular_1.GetCamera())

celular_1.SetCamera("10000MP")

print(celular_1.GetCamera())
