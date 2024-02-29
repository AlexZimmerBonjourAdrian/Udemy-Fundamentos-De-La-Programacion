class Player:
     def __init__(self, Nombre, Life):
        self.Nombre = Nombre
        self.Life = Life

     def getNombre(self):
         return self.Nombre
        
     def setNombre(self,Nombre):
         self.Nombre = Nombre

     def getLife(self):
         return self.Life
        
     def setLife(self,life):
         self.Life = life

     def ImprimirMesanje(self):
        print("Esta funcion probiene del padre")
