#Creacion de clases y como interactuan entre si con una clase principal sin metodos mas que los setter y getters

    
    #variables
class Celular():
    
    #variables
    def __init__(self, marca,modelo="Desconocido",camera = "100MP"):
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


class Telefonica():
    def __init__(self, servicio,marca,Plan,Celular= None):
        self.servicio = servicio
        self.marca = marca
        self.Plan = Plan
        self.Celular = Celular 
    
    def SetMarca(self, Marca):
            self.marca = Marca
        
    def GetMarca(self):
            return self.marca

        
    def SetPlan (self, plan):
            self.Plan = plan
        
    def GetPlan(self):
            return self.Plan


        
    def SetCelular(self, celular):
            self.Celular = celular
        
    def GetCelular(self):
            return self.Celular


    def cambiarDeCompania(self,celular):
        celular.SetMarca(self.marca)
        return Celular



celular_1 = Celular("sansung", "S13", "40PMX")
print(celular_1.GetMarca())

nueva_telefonica = Telefonica("Telefonica", "Tigo", "Ahorro", celular_1)

#print(nueva_telefonica.GetCelular().GetMarca())



nueva_telefonica.cambiarDeCompania(celular_1)

print(nueva_telefonica.Celular.GetMarca())
print(nueva_telefonica.Celular.SetMarca("OtraCompania"))
print(nueva_telefonica.Celular.GetMarca())

print(celular_1.GetMarca())
