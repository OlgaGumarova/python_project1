# с циклом while:
list_1 = [1,1]
i = 2
while i < 15:
    a = list_1[i-1] + list_1[i-2]
    list_1.append(a)
    i += 1
print(list_1)
# с циклом for:
list_2 = [1,1]
i = 2
for el in list_2:
    if i == 15:
        break
    a = list_2[i - 1] + list_2[i - 2]
    list_2.append(a)
    i += 1
print(list_2)

