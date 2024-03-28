#classes structure
#Las clases son objetos que tiene tanto su propia definicion y comportamiento
#Esta es una clase celular
#esto es una clase limpia sin muchas cosas que el faltan

#Esto no funciona ya que las clases nesecitan un constructor para funcionar, esto trae el problema de que no se peuden llamar funciones
# class celular_2():
    
#     #variables de la clase
#     marca = "Sansung"
#     modelo = "S23"
#     camera = "40MP"

#     #metodos
#     def mostrarMarca():
#         print(marca)
#     def mostrarModelos():
#         print(modelo)

#     def mostrarCamera():
#         print(camera)


# Celular1 = celular_2()

# Celular1.mostrarCamera()
# Celular1.mostrarModelos()
# Celular1.mostrarCamera()
#Esta seccion esta fuera de la clase celular y lo que e hecho fue crear varios celulares

class Celular:
    #En este caso el constructor define las variables que pose la clase para cuando se cree el objeto este sepa como crearlo
    #Self es una palabra reservada para saber que se refiere a si misma
    def __init__(self, marca, modelo, camera):
        self.marca = marca
        self.modelo = modelo
        self.camera = camera

    def mostrarMarca(self):
        print(self.marca)

    def mostrarModelos(self):
        print(self.modelo)

    def mostrarCamera(self):
        print(self.camera)

#Se crea un celular, y se llama para revisar los datos

celular1 = Celular("Samsung", "S23", "40MP")
celular1.mostrarMarca()
celular1.mostrarModelos()
celular1.mostrarCamera()