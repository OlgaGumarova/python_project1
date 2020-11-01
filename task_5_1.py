while True:
    numb_1 = int(input('Введите первое число:'))
    sign = input('Введите знак:')
    numb_2 = int(input('Введите второе число:'))
    if sign != '+' and sign != '-' and sign != '*' and sign != '/' and sign != '0':
        print('Вы ввели неверный знак операции!')
        continue
    elif sign == '/' and numb_2 == 0:
        print('На ноль делить нельзя!')
        continue
    elif sign == '+':
        z = numb_1 + numb_2
        print(z)
    elif sign == '-':
        z = numb_1 - numb_2
        print(z)
    elif sign == '*':
        z = numb_1*numb_2
        print(z)
    elif sign == '/':
        z = numb_1/numb_2
        print(z)
    elif sign == '0':
        break


