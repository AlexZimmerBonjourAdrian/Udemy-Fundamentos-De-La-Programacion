#Ejercicio Calcuar el porcentaje de un monto
#Conversion de unidad de medidas de centimetros a pulgadas
#Verificar si dos numeros enteros son diferentes
i = 0
exit = False

numero_1=0.0
numero_2=0.0
Resultado = 0.0




#Funcion de calcular procentaje de un monton y cuanto es ste
def CalcularProcentaje():
    numero_1 = int(input("Ingrese un monto: "))
    numero_2 = int(input("Ingrese un procentaje: "))
    Resultado = (numero_2 /100 ) * numero_1
    print("Esta es el procentaje del monto: "  + (str)(Resultado))

#Funcion de convertir centimetros a pulgadas
def ConvertirCmmToItchs():
    numero_1 = int(input("Ingrese la medida en centimetros: "))
    Resultado = (numero_1 * 2.54) 
    print("Esta es la conversion en pulgadas: "  + (str)(Resultado))

#verificar si dos numeros son distitios
def verificarSiDosNumerosSonDistintos():
    numero_1 = int(input("Ingrese un numero1: "))
    numero_2 = int(input("Ingrese un numero2: "))
    Resultado = (bool)(numero_1 != numero_2) #Python permite hacer polimorfismo sin mucho esfuero: esto hay que ser cuidadoso en poo
    print("verificar Si Dos Numeros Son Distintos: "  + (str)(Resultado))
    
def Salir():
    exit = True
    print("Adios!.")


#Este menu es mas para su comodidad, si quieren prbarlo simplemente comenten el menu y ejecuten funcion por funcion
while not exit :
    #Mostrar menu
    print("Menu Normal")
    print("1.Calcular Procentaje")
    print("2.Convertir Cmm To Itchs")
    print("3.Verificar Si Dos Numeros Son Distintos")
    print("4.Salir")
   
    #Pedir opcion
   
    i = int(input("Ingrese opcion: "))

    #Ejecutar procedimiento
    if (i == 1):
            CalcularProcentaje()
    elif  (i == 2):
            ConvertirCmmToItchs()
    elif  i == 3:
            verificarSiDosNumerosSonDistintos()
    elif(i == 4):
            Salir()
            break

    else:
        print("El comando no es valido")
        print(" ")

