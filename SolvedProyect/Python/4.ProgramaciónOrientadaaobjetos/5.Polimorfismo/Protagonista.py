from Player import Player

class Protagonista(Player):
     def __init__(self, Nombre,Life,IsAttacando,IsSword):
        super().__init__(Nombre,Life)
        self.IsAttacando = IsAttacando
        self.IsSword = IsSword

     def getNombre(self):
         return self.IsSword
        
     def setNombre(self,isSword):
         self.IsSword= isSword

     def getIsAttacando(self):
         return self.IsAttacando
        
     def setIsAttacando(self,isAttacando):
         self.IsAttacando = isAttacando
      