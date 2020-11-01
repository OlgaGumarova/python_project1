m = int(input('Введите целое число:'))
n = int(input('Введите второе целое число, больше предыдущего:'))
ls = [i for i in range(m, n+1)]
print(ls)
for el in ls:
    i = 2
    print(f'{el}:')
    while i < el:
        if el%i == 0:
            print(f'{i}')
        i += 1

