str_1 = input('Введите строку')
central_letter = str_1[len(str_1)//2]
print(central_letter)
if central_letter == str_1[0]:
    print(str_1[1:-1])


