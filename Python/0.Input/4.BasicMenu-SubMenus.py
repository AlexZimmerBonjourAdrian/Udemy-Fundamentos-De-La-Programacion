i = 0
exit = False

def DecirHola():
        print("Hola Mundo")
        print(" ")
        PrincipalMenu()

def CalcularmeUnNumero():
    numero_1 = int(input("Ingrese un numero1: "))
    numero_2 = int(input("Ingrese un numero2: "))

    numero_1 + numero_2 
    print("Esta es la suma: "  + (str)(numero_1 + numero_2))
    print(" ")
    i = 0
    PrincipalMenu()

def Salir():
    exit = True
    print("Adios!.")
    
def PrincipalMenu():
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
           
    else:
        print("el comando no es valido")
        print(" ")

def SecundarioMenu():
         #Mostrar menu
    print("Menu Secundario")
    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Division")
    print("3.Salir")
   
    #Pedir opcion
   
    i = int(input("Ingrese opcion: "))

    #Ejecutar procedimiento
#     if (i == 1):
#             DecirHola()
#     elif  (i == 2):
#             CalcularmeUnNumero()
#     elif  i == 3:
#             Salir()
           
#     else:
#         print("el comando no es valido")
#         print(" ")

def TercerioMenu():
         #Mostrar menu
    print("Menu Terceario")
    print("1.DarReceta")
    print("2.Preparar receta")
    print("3.Salir")
   
    #Pedir opcion
   
#     i = int(input("Ingrese opcion: "))

#     #Ejecutar procedimiento
#     if (i == 1):
#             DecirHola()
#     elif  (i == 2):
#             CalcularmeUnNumero()
#     elif  i == 3:
#             Salir()
           
#     else:
#         print("el comando no es valido")
#         print(" ")

def submenuCalculadora():
        numero_1 = int(input("Ingrese un numero1: "))
        numero_2 = int(input("Ingrese un numero2: "))

        numero_1 + numero_2 
        print("Esta es la suma: "  + (str)(numero_1 + numero_2))
        print(" ")
        i = 0
        PrincipalMenu()
        
while exit != True :
        PrincipalMenu()
        
        i = int(input("Ingrese opcion: "))
        break
   