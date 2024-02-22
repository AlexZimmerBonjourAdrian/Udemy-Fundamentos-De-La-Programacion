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
     def __init__(self, Nombre,IsAttacando,IsSword):
        super().__init__(Nombre)
        self.IsAttacando = IsAttacando
        self.IsSword = IsSword


# Crear objetos de las diferentes clases
protagonista = Protagonista_1("Protagonista", False , False)
mascota = Mascota_1("Mascota", False, False)
companiero = Companiero_1("Companiero",  False, False)

# Utilizar el método ImprimirMensaje de la clase base Player
print(protagonista.getNombre())
print(mascota.getNombre())
print(companiero.getNombre())

# Utilizar el método ImprimirMensaje de la clase base Player
protagonista.ImprimirMesanje()
mascota.ImprimirMesanje()
companiero.ImprimirMesanje()