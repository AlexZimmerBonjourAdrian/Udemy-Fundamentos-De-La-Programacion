from Player import Player

class Mascota(Player):
     def __init__(self, Nombre,Life,IsAttacando, IsReclutado ):
        super().__init__(Nombre,Life)
        self.IsAttacando = IsAttacando
        self.IsReclutado = IsReclutado