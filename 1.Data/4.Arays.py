#Python maneja los arrays como listas
array_1 = [1,2,3,4,5,6,7,8] #Normal
list_2 = ["Hola", "Adios", 3,5,10,0.2] #Combinado esto es por uqe los trata de listas
list_3 = [] # Lista vacio
print("irpimir elementos de list_1")
print(" ")
print(array_1[0])  # Imprime el primer elemento del array(1)
print(array_1[2])  # Imprime el primer elemento del array(1)
print(array_1[5])  # Imprime el primer elemento del array(1)
print(array_1)


print("imprimir elementos de list_2")
print(" ")
print(list_2[0])
print(list_2[2])
print(list_2[5])
print(list_2)

print("agregar un elemento a la list_3")
#se agregan un elemento
list_3.append(30)
print("agregar varios lementos un elemento a la list_3")
#se agregan varios elementos
list_3.extend([30,40,70,30])
print(list_3)

#Elmina e ultimo elemento
list_3.pop()
print(list_3)

#Remueve el elemento que indica el indixe
list_3.remove(list_3[0])
print(list_3)

print("imprimir elementos de list_3")
print(" ")

print("List_3: "  + (str)(list_3[0]))
print("List_3: "  + (str)(list_3[1]))
print("List_3: "  + (str)(list_3[2]))





