#como estructurar funciones

 #tres ejemplos de funciones
class TempAuto():
      def __init__(self, marca, modelo):
            self.marca = marca
            self.modelo = modelo
      
      def cambiarDeMarca(self):
            self.marca = "changoles"
            self.marca = "MK1"
      


#esto seria una funcion simple
#self es nesesario ya que se usa para hacer referencia a este objeto y tambien referenciar a los variables de este mismo
def funcion_1(self):
    pass

#esto seria una funcion , con carios parametros y devuelve el primero que se le agregue
def funcion_2(self, numero_1, numero_2):
   
   #devuelve la primera variable
    # return numero_1

   #devuelve una operacion entre los numeros
   # return numero_1 + numero_2

   #esto devuelve un bool de una operacion logica
    return numero_1 >= numero_2 
    
auto_1 = TempAuto("Chebrolet", "B13")
auto_2 = TempAuto("Chebrolet", "B13")
auto_3 = TempAuto("Chebrolet", "B13")
#esto seria una funcion simple
def funcion_3(self, tempAuto):
    print(tempAuto.marca)
    print(tempAuto.modelo)

def funcion_4(self, tempAuto):
    print(tempAuto.marca)
    print(tempAuto.modelo)

    tempAuto.cambiarDeMarca()

    print(tempAuto.marca)
    print(tempAuto.modelo)

funcion_3(auto_1)

funcion_4(auto_2)
