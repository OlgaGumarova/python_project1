# c циклом while:
list_1 = [1,2,3,4,5]
list_2 = [1,2,3,4,5]
i = 0
while i < len(list_1):
    list_2[i-1] = list_1[i]
    i += 1
print(list_2)
# с циклом for:
i = 0
for el in list_1:
    list_2[i-1] = list_1[i]
    i += 1
print(list_2)




