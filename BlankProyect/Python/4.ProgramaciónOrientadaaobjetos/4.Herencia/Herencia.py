#Herencia clase padre
class Player_1:
     def __init__(self, Nombre):
        self.Nombre = Nombre

     def getNombre(self):
         return self.Nombre
        
     def setNombre(self,Nombre):
         self.Nombre = Nombre

     def ImprimirMesanje(self):
        print("Esta funcion probiene del padre")

class Companiero_1(Player_1):
     def __init__(self, Nombre,IsAttacando, IsReclutado ):
        super().__init__(Nombre)
        self.IsAttacando = IsAttacando
        self.IsReclutado = IsReclutado


class Mascota_1(Player_1):
     def __init__(self, Nombre,IsAttacando, IsReclutado ):
        super().__init__(Nombre)
        self.IsAttacando = IsAttacando
        self.IsReclutado = IsReclutado

class Protagonista_1(Player_1):
     def __init__(self, Nombre,IsAttacando,IsSword= False):
        super().__init__(Nombre)
        self.IsAttacando = IsAttacando
        self.IsSword = IsSword



protagonista = Protagonista_1("Protagonista",False)
mascota = Mascota_1("Mascota",False,False)
companiero = Companiero_1("Companiero", False,False)

#Muestro los nombres de los objetos con sus geter
print(protagonista.getNombre())
print(mascota.getNombre())
print(companiero.getNombre())

#Utilizo el metodo imprimir mensaje de la clase Player 
protagonista.ImprimirMesanje()
mascota.ImprimirMesanje()
companiero.ImprimirMesanje()


