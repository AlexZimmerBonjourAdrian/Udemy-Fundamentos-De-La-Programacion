from Player import Player
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

companiero = Companiero("Companiero",100 , False, False)
