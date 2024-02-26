matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

print(matrix[0][0])
print(matrix[1][2])
#las listas cuentan desde el 0 asi que seria asi seria de 0 a n-1 de largo

print(matrix)
print(matrix[0])

matrix_mas_clara = [[1,2,3],
                  [4,5,6]]
print(matrix_mas_clara)

def print_matrix_whith_index():
    for i in range(len(matrix_mas_clara)):
         for j in range(len(matrix_mas_clara[i])):
            print(matrix_mas_clara[i][j], end = ' ')
         print(" ")

print_matrix_whith_index()