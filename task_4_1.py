#вариант с циклом while:
list_1 = [1,2,3,4,5,6,7,8]
i = 0
while i < len(list_1):
    list_1[i] = list_1[i]*-2
    i += 1
print(list_1)
# вариант с циклом for:
list_1 = [1,2,3,4,5,6,7,8]
i = 0
for el in list_1:
    list_1[i] = el * -2
    i += 1
print(list_1)

