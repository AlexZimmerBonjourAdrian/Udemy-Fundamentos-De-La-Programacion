#Switch

numero_switch = int(input("Ingrese un numero: "))
x = 5

#esto es el switch de python llamado match

# funciona de la siguiente manera, tengo un dato de entrada y lo compara en diferentes casos
#esto da como resultado multiples respuestas y una generica si ese valor no existe, esto es mas ligero que un if 
#no soporta operadores logicos solo entradas de valor str, int
print("match X")
match x:
        case 0:
            print("Uno")
        case 2:
            print("Dos")
        case 3:
            print("Tres")
        case 4:
            print("Cuatro")
        case 5:
            print("cinco")
        case _:
            print("Numero fuera de rango")

print("match numero_switch")
match numero_switch:
        case 0:
            print("Uno")
        case 2:
            print("Dos")
        case 3:
            print("Tres")
        case 4:
            print("Cuatro")
        case 5:
            print("cinco")
        case _:
            print("Numero fuera de rango")
