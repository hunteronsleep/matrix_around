'''На вход подаётся матрица (двумерный массив). Все элементы матрицы - целые числа.
Поверните матрице на 90 градусов по часовой стрелке.'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_2 = [
    [1, 2],
    [4, 5],
    [7, 8]
]

def roatate_matrix(matrix):
    n = len(matrix)
    roated_matrix = [[0 for _ in range (n)] 
    for _ in range(n)]

    for i in range(n):
        for j in range(n):
            roated_matrix[j][n-1-i] = matrix[i][j]
    return roated_matrix


roatated = roatate_matrix(matrix)
for row in roatate_matrix(matrix):
    print(row)