from random import randint
n = 3
matrix = [[randint(1,9) for j in range(n)]for i in range(n)]
print(matrix)
i = 0
for el in matrix[i]:
    a = matrix[i].index(max(matrix[i]))
    matrix[i][i], matrix[i][a] = matrix[i][a], matrix[i][i]
    i += 1
print(matrix)
