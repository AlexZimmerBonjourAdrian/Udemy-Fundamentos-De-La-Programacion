#bucles for

#python controla los for, como si fuera foreach 
#forReach
matrix_mas_clara = [[1, 4, 5], 
                    [-5, 8, 9]]
fruits = ["manzana", "plátano", "pera"]
for fruits in fruits:
    print(fruits)

print(" ")

#For range
for i in range(1, 11):
    print(i)

print(" ")


#este es un mejor ejemplo 
#se recorre el arngo de la matrix por las coulmnas
#luego las filas
def print_matrix_whith_indices():
    for i in range (len(matrix_mas_clara)):
        for j in range(len(matrix_mas_clara[i])):
            print(matrix_mas_clara[i][j], end=' ')
        print()




#este es un ejemplo en c++
# for(i = 0; i < fruits.count; i++):
#{

#}

