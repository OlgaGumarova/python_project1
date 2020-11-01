numb_guests = int(input('Введите число гостей:'))
if numb_guests >= 50:
    print('ресторан')
elif numb_guests < 50 and numb_guests >= 20:
    print('кафе')
else:
    print('дом')

