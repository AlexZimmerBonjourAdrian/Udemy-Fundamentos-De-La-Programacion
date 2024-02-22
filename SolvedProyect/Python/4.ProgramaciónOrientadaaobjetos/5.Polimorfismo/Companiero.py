from Player import Player
class Companiero(Player):
    def __init__(self, Nombre, Life,IsAttacando, IsReclutado):
        super().__init__(Nombre,Life)
        self.IsAttacando = IsAttacando
        self.IsReclutado = IsReclutado

    def getNombre(self):
         return self.IsAttacando
        
    def setNombre(self,isAttacando):
         self.IsAttacando= isAttacando

    def getIsReclutado(self):
         return self.IsReclutado
        
    def setLife(self,isReclutado):
         self.IsReclutado = isReclutado

companiero = Companiero("Companiero",100 , False, False)


