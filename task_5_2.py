numb = list(input('Введите число:'))
from functools import reduce
summ_numb = reduce(lambda x, y: int(x) + int(y), numb, 0)
print(summ_numb)
mult_numb = reduce(lambda x, y: int(x) * int(y), numb, 1)
print(mult_numb)

