from Player import Player
class Companiero(Player):
    def __init__(self, Nombre, Life,IsAttacando, IsReclutado):
        super().__init__(Nombre,Life)
        self.IsAttacando = IsAttacando
        self.IsReclutado = IsReclutado


companiero = Companiero("Companiero",100 , False, False)


