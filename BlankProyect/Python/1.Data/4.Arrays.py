#python toma a los arrays como listas

array_1 = [1,2,3,4,5,6,7,8,9]
lista_2 = ["Hola", "Adios", 3,5,10,0.2]
lista_3 = [] #Lista vacia

# print("imprimir elementos lista_1")
# print(" ")
# print(array_1[0])
# print(array_1[1])
# print(array_1[2])

print(lista_2)
print(array_1)
print(lista_3)

#como agregr quitar o modificar elementos en los arrays

#agregar
lista_3.append(30) #agrega solo un elemento a la vez

lista_3.extend([30,40,70,30,80]) #me agrega todos los elementos que quiero

print(lista_3)

#eliminar
lista_3.pop() #elimina el ultimo elemento

lista_3.remove(lista_3[0]) #elimina el elemento que se encuentra en esta posicion

print(lista_3)
#NOTA IMPORTANTE, al momento de eiminar python reacomoda los objetos, en lenguajes mas abajo nivel usted debera controlar si hay elementos nullos y elimunarlos con algoritmos de busqueda

#modificar un elemento 
lista_3[0] = 60


print(lista_3)