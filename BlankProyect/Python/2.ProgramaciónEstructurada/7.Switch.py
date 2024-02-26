#Switch o match en python



x=1

match x:
    case 1: 
        print("uno")
    case 2: 
        print("dos")
    case 3: 
        print("tres")
    case 4: 
        print("cuatro")
    case 5: 
        print("cinco")
    case _:
        print("En numero no es valido")

numeor_5 = int(input("Ingrese Numero"))

#funciona con int o con strings pero no soporta operadores logicos
match numeor_5:
    case 0: 
        print("uno")
    case 2: 
        print("dos")
    case 3: 
        print("tres")
    case 4: 
        print("cuatro")
    case 5: 
        print("cinco")
    case _:
        print("En numero no es valido")