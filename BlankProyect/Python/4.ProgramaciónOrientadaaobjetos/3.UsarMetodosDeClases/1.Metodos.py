#Creacion de clases e que usen metodos especiales con un pequeño programa
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
     
     def CheckVida(self):
        if(self.getLife() <= 0):
            print("Death")
        else:
            print("Sigo Vivo")



#Creacion de clases e que usen metodos especiales con un pequeño programa
class Mascota(Player):
     def __init__(self, Nombre,Life ):
        super().__init__(Nombre,Life)
        


class Companiero(Player):
    def __init__(self, Nombre, Life,IsAttacando, IsReclutado):
        super().__init__(Nombre,Life)
        self.IsAttacando = IsAttacando
        self.IsReclutado = IsReclutado

    def getIsAttacando(self):
         return self.IsAttacando
        
    def setIsAttacando(self,isAttacando):
         self.IsAttacando= isAttacando

    def getIsIsReclutado(self):
         return self.IsReclutado
        
    def setIsReclutado(self,isReclutado):
         self.IsReclutado = isReclutado




class Enemy():
      def __init__(self, Nombre):
        self.Nombre = Nombre
        self.damage= 30
      
      def apllyDamage(self,Object, damage):
         Object.setLife(Object.getLife() - damage)

companiero = Companiero("Companiero", 100, False,False)
mascota = Mascota("Mascota", 100 )
enemy = Enemy("Enemy")

enemy.apllyDamage(companiero,100)

companiero.CheckVida()

print(companiero.getLife())


enemy.apllyDamage(mascota,50)

print(mascota.getLife())

mascota.CheckVida()


  

