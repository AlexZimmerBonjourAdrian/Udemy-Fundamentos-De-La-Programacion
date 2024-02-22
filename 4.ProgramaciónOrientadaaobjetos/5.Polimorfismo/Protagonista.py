from Player import Player

class Protagonista(Player):
     def __init__(self, Nombre,Life,IsAttacando,IsSword):
        super().__init__(Nombre,Life)
        self.IsAttacando = IsAttacando
        self.IsSword = IsSword
      