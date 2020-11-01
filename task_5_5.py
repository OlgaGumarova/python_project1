from random import randint
ls = [randint(1,100) for i in range(0,19)]
from array import array
numbers = array('i', ls)
print(numbers)
print(ls)
for el in numbers:
    i = 0
    while i < len(ls):
        if el > ls[i]:
            del ls[i]
            i -= 1
        i += 1
print(ls)
i = 0
while i < len(numbers):
    if numbers[i]%2 == 0:
        numbers[i] = ls[0]
    i += 1
print(numbers)


