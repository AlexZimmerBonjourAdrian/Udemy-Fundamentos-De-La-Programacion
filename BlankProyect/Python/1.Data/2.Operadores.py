import math

numero_1 = 0
numero_2 = 0

restultado = 0

numero_1 = (int)(input("Ingrese el numero_1: "))
numero_2 = (int)(input("Ingrese el numero_2: "))

#suma
restultado = numero_1 + numero_2
print("El resultado de la suma es : " + (str)(restultado))


#Resta
restultado = numero_1 - numero_2
print("El resultado de la suma es : " + (str)(restultado))
#Division
restultado = numero_1 / numero_2
print("El resultado de la suma es : " + (str)(restultado))
#Multiplicacion
restultado = numero_1 * numero_2
print("El resultado de la suma es : " + (str)(restultado))

#Operaciones Extras

#Modulo (Resto de la divicion) %
Resultado = numero_1 % numero_2
print("Esta es la Modulo: "  + (str)(Resultado))

#Potencia
Resultado = numero_1 ** numero_2
print("Esta es la Potencia: "  + (str)(Resultado))

#Raiz Cudrada:
Resultado = numero_1 ** (1/numero_2)
print("Esta es la Raiz Cudrada: "  + (str)(Resultado))

#Logartismo
Resultado = math.log(numero_1,numero_2)
print("Esta es la Logartismo: "  + (str)(Resultado))

