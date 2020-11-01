n = int(input('Введите число:'))
from functools import reduce
def fact2(n):
    if n%2 != 0:
        ls_1 = [i for i in range(1, n + 1, 2)]
        fact_n = reduce(lambda a, b: a*b, ls_1, 1)
        return fact_n
    if n%2 == 0:
        ls_2 = [i for i in range(2, n + 1, 2)]
        fact_n = reduce(lambda a, b: a * b, ls_2, 1)
        return fact_n
print(fact2(n))

