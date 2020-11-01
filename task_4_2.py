#вариант с циклом while:
list_1 = [1,2,3,4,5,6,7,8,9,10]
i = 0
numb_of_even = 0
while i < len(list_1):
    if list_1[i]%2 == 0:
        numb_of_even += 1
    i += 1
print(numb_of_even)
#вариант с циклом for:
list_1 = [1,2,3,4,5,6,7,8,9,10]
numb_of_even = 0
for el in list_1:
    if el%2 == 0:
        numb_of_even += 1
print(numb_of_even)

