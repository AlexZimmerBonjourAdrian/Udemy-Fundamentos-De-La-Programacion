class celular():
        def __init__(self,marca,modelo = "Desconocido",camera = "100MP"):
                self.marca=marca
                self.modelo = modelo
                self.camera = camera
        def SetMarca(self, Marca):
            self.marca = Marca
        def GetMarca(self):
            return self.marca
        
        def SetModelo(self, Modelo):
            self.modelo = Modelo
        def GetModelo(self):
            return self.modelo
        
        def SetCamera(self, Camera):
            self.camera = Camera
        def GetCamera(self):
            return self.camera
        
        def __del__(self):
                print("Destoyiong Object...")

class Telefonica():
        def __init__(self, servicio, marca,plan,celular= None):
            self.servicio = servicio
            self.marca = marca
            self.plan = plan
            self.celular = celular

        def SetServicio(self, Servicio):
                self.servicio = Servicio
        def GetServicio(self):
                self.servicio
        def SetMarca(self, Marca):
                self.marca = Marca
        def GetMarca(self):
                self.marca
        def SetPlan(self, Plan):
                self.plan= Plan 
        def GetPlan(self):
                self.plan 
        def SetCelular(self, Celular):
                self.celular = Celular
        def GetCelular(self):
                self.celular

        def cambiarDeCompania(self):
                self.celular.SetMarca(self.marca)
                return celular
        
        #  def cambiarDeCompania(self, Celular):
        #         celular.SetMarca(self.marca)
        #         return celular

        def __del__(self):
             print("Destoyiong Object...")
        

celular_1 = celular("sansung","S13", "40PMX")
print(celular_1.GetMarca())
        
nueva_telefonica = Telefonica("Telefonica", "Tigo" , "Ahorro", celular_1)
print(nueva_telefonica.cambiarDeCompania())
print(celular_1.GetMarca())

print(" ")
print(nueva_telefonica.celular.GetMarca())
print(nueva_telefonica.celular.SetMarca("OtraCompania"))
print(nueva_telefonica.celular.GetMarca())
print(" ")
print(celular_1.GetMarca())