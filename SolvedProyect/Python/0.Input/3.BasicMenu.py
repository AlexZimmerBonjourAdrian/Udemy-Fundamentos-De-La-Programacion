i = 0
exit = False

def DecirHola():
        print("Hola Mundo")
        print(" ")

def CalcularmeUnNumero():
    numero_1 = int(input("Ingrese un numero1: "))
    numero_2 = int(input("Ingrese un numero2: "))

    numero_1 + numero_2 
    print("Esta es la suma: "  + (str)(numero_1 + numero_2))
    print(" ")
    i = 0

def Salir():
    exit = True
    print("Adios!.")
    

while not exit :
    #Mostrar menu
    print("Menu Normal")
    print("1.Decir hola")
    print("2.Sumar dos numero")
    print("3.Salir")
   
    #Pedir opcion
   
    i = int(input("Ingrese opcion: "))

    #Ejecutar procedimiento
    if (i == 1):
            DecirHola()
    elif  (i == 2):
            CalcularmeUnNumero()
    elif  i == 3:
            Salir()
            break
    else:
        print("el comando no es valido")
        print(" ")
