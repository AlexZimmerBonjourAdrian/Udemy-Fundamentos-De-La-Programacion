from Mascota import Mascota
from Companiero import Companiero
from Protagonista import Protagonista

protagonista = Protagonista("Protagonista",100,False,False)
mascota = Mascota("Mascota",100)
companiero = Companiero("Companiero",100,False,False)

#Utilizar el metodo imprimir mensaje de la clase base Player
print(protagonista.getNombre())
print(mascota.getNombre())
print(companiero.getNombre())

protagonista.ImprimirMesanje()
mascota.ImprimirMesanje()
companiero.ImprimirMesanje()

protagonista = mascota
companiero = protagonista
mascota = companiero

print(protagonista.getNombre())
print(mascota.getNombre())
print(companiero.getNombre())

#al momento de llamarlo da error por 
# print(companiero.getIsReclutado())

