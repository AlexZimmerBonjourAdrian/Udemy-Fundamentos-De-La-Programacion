#Recursividad
#Recursividad normal
def RecursividadNomal():
    print("RecursividadNormal")
    RecursividadNomal()

def RecursividadConAtributos(n):
    if(n <= 5):
        n_Temp = n + 1
    return RecursividadConAtributos(n_Temp)

def Sumatorio(n):
    if n==0:
        return 0
    else:
        return n + Sumatorio(n-1)
