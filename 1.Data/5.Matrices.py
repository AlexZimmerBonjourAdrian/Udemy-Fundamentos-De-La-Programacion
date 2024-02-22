#notas pip install numpy si no esta instalado
#notes pip install matplotlib si no esta instalado
import numpy as np
import matplotlib.pyplot as plt
matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix[0][0]) #imprime el elemento en la primera fila y columna
print(matrix[1][2]) #inprime el sengundo elemento en la segunda flla y tercera columna

#otra forma de dibujarlo
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

#una forma mas comoda de visualizarlo
matrix_mas_clara = [[1, 4, 5], 
                    [-5, 8, 9]]

print(matrix_mas_clara)

print(' ')

matrix_mas_clara = [[1, 4, 5], 
                    [-5, 8, 9]]

def print_matrix_whith_indices():
    for i in range (len(matrix_mas_clara)):
        for j in range(len(matrix_mas_clara[i])):
            print(matrix_mas_clara[i][j], end=' ')
        print()

print_matrix_whith_indices()

