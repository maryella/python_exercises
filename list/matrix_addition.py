# Matrix Addition
matrix1 = [[1, 3], [2, 4]]
matrix2 = [[5, 2], [1, 0]]
result = []
i = 0

while i <= (len(matrix1) - 1):
    n = 0
    new_matrix = []
    while n < len(matrix1[i]):
        new_num = matrix1[i][n] + matrix2[i][n]
        new_matrix.append(new_num)
        n += 1
    result.append(new_matrix)
    i += 1

print(result)
