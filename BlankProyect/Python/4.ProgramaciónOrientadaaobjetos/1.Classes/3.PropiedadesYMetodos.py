class Celular():
    
    #variables
    def __init__(self, marca,modelo,camera = "100MP"):
        self.marca = marca
        self.modelo = modelo
        self.camera = camera
        #self.otro = None
        self.otro = 5

        
    #Metodo

    def mostrarMarca(self):
        print(self.marca)
    
    def mostrarModelo(self):
        print(self.modelo)

    def mostrarCamera(self):
        print(self.camera)

    def mostrarOtro(self):
        print(self.otro)

celular_1 = Celular("Sansung", "S23", "50MP")
celular_1.mostrarMarca()
celular_1.mostrarModelo()
celular_1.mostrarCamera()
# celular_1.mostrarOtro()


