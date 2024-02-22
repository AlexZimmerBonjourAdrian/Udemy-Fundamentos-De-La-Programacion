# from Player import Protagonista, Mascota, Companiero
from Mascota import Mascota
from Companiero import Companiero
from Protagonista import Protagonista


protagonista = Protagonista("Protagonista",100 ,False , False)
mascota = Mascota("Mascota", 100 ,False, False)
companiero = Companiero("Companiero", 100 , False, False)

# Utilizar el método ImprimirMensaje de la clase base Player
print(protagonista.getNombre())
print(mascota.getNombre())
print(companiero.getNombre())

# Utilizar el método ImprimirMensaje de la clase base Player
protagonista.ImprimirMesanje()
mascota.ImprimirMesanje()
companiero.ImprimirMesanje()

protagonista = mascota
companiero = protagonista
mascota = companiero

#

print(protagonista.getNombre())
print(mascota.getNombre())
print(companiero.getNombre())

