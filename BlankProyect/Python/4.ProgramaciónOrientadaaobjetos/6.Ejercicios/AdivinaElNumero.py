#Crear un juego de adivinar donde esta una esfera
import sys
import random

class Game:
     def __init__(self, intentos=3):
        self.intentos = intentos
        self.number = None

    #Start
     def StartGame(self):
        self.numero = self.RandomNumber()
        self.PlayGame()

    #clase principal del juego
    #GameLoop o Update
     def PlayGame(self):
            print("Tienes" +  " " + (str)(self.intentos)  + " numero de Intentos ")
            print(" ")
            selected = self.SelectNumber()
            self.CharacterBarcks(selected,self.numero)
            self.LoseCondition()
            
        
 #Logica del juego
     def RandomNumber(self):
            RandomNumber = (int)(random.randrange(0,10))
            print(" ")
            print("Ya pense en un numero")
            
            return RandomNumber
            
        #Win COndition
     def WinCondition(self): 
            print(" ")
            print("Ganaste felicitaciones!")

            print(" ")
            print("Quires volver a jugar?")
            
            Opciones = str(input("Seleccione entre y(new Game) o n(Exit): "))

            
            if(Opciones == "Y" or Opciones == "y"):
                self.intentos = 3
                self.IStartGame = False
                self.StartGame()
            elif(Opciones == "N" or Opciones == "n"):
                sys.exit()
                return
            else:
                print(" ")
                print("La opcion no es valida")
                self.WinCondition() 
        
        
        #Lose Condition
     def LoseCondition(self):
            self.intentos -=  1
            if(self.intentos <= 0):
                print("Perdiste, lo lamento")
                sys.exit()
            else:
                self.PlayGame()
    #Logica del juego
     def SelectNumber(self):
            print(" ")
            print("Se eligio un numero de 0 al 10")
            var = input("Ingrese el numero a adivinar: ")
            if(var.isdecimal()):
                numero = int(var)
                return numero
            else: 
                print("No es un numero valido")
                self.PlayGame()
            return numero
 #Logica del juego
     def CharacterBarcks(self, numero_ingresado, numero_a_adivinar):
           
            print("Adivina que numero estoy pensando")
            if(numero_ingresado > numero_a_adivinar):
                print(" ")
                print("muy alto")
              
            
            elif (numero_ingresado < numero_a_adivinar):
                print(" ")
                print("muy Bajo")
              
            
            else:
                self.WinCondition()
                print(" ")
                print("Adios!")


game = Game(3)
while True:
   game.StartGame()
   break

   

 
