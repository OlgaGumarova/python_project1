# 1.создание матрицы
from random import randint
matrix = [[randint(1,9) for i in range(3)] for j in range(4)]
print(matrix)
# 2.максимальный элемент матрицы
i = 0
ls_1 = []
while i < 4:
    ls_1.append(max(matrix[i]))
    i += 1
max_el = max(ls_1)
print(max_el)
#  3.минимальный элемент матрицы
i = 0
ls_2 = []
while i < 4:
    ls_2.append(min(matrix[i]))
    i += 1
min_el = min(ls_2)
print(min_el)
# 4.сумма всех элементов матрицы
from functools import reduce
summ_matrix = reduce(lambda x,y: x + y, matrix)
summ_el = reduce(lambda x, y: x + y, summ_matrix)
print(summ_el)
# 5.индекс ряда с максимальной суммой элементов
ls_max = []
i = 0
while i < 4:
    ls_max.append(reduce(lambda x,y: x+y, matrix[i]))
    i += 1
print(ls_max.index(max(ls_max)))
# 6.индекс колонки с максимальной суммой элементов
d = list(zip(*matrix))
col_max = []
i = 0
while i < 3:
    col_max.append(reduce(lambda x,y: x + y, d[i]))
    i += 1
print(col_max.index(max(col_max)))
# 7.индекс ряда с минимальной суммой элементов
ls_min = []
i = 0
while i < 4:
    ls_min.append(reduce(lambda x,y: x+y, matrix[i]))
    i += 1
print(ls_min.index(min(ls_min)))
# 8.индекс колонки с минимальной суммой элементов
col_min = []
i = 0
while i < 3:
    col_min.append(reduce(lambda x,y: x + y, d[i]))
    i += 1
print(col_min.index(min(col_min)))
# 11.две новые матрицы
k = 4
l = 3
matrix_a = [[randint(1,9) for i in range(k)] for j in range(l)]
matrix_b = [[randint(1,9) for i in range(k)] for j in range(l)]
print(matrix_a)
print(matrix_b)



