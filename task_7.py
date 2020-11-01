def inch_cm(value):
    return value * 2.54
def cm_inch(value):
    return value * 0.3937
def mile_km(value):
    return value * 1.609
def km_mile(value):
    return value * 0.6214
def lb_kg(value):
    return value * 0.4535923745
def kg_lb(value):
    return value * 2.20462
def oz_g(value):
    return value * 28.3495231
def g_oz(value):
    return value * 0.035274
def gal_lit(value):
    return value * 3.78541
def lit_gal(value):
    return value * 0.219969
def pt_lit(value):
    return value * 0.473176
def lit_pt(value):
    return value * 2.11338
print('Выберите один из вариантов операций:')
print('1. Дюймы в сантиметры')
print('2. Сантиметры в дюймы')
print('3. Мили в километры')
print('4. Километры в мили')
print('5. Фунты в килограммы')
print('6. Килограммы в фунты')
print('7. Унции в граммы')
print('8. Граммы в унции')
print('9. Галлон в литры')
print('10. Литры в галлоны')
print('11. Пинты в литры')
print('12. Литры в пинты')
while True:
    numb = int(input('Введите номер операции:'))
    value = int(input('Введите число'))
    if numb < 0 or numb > 12:
        print('Введите верный номер операции')
    list_of_def = [inch_cm(value), cm_inch(value), mile_km(value),
                   km_mile(value),lb_kg(value), kg_lb(value),oz_g(value),
                   g_oz(value), gal_lit(value),lit_gal(value), pt_lit(value),
                   lit_pt(value)]
    i = 0
    for el in list_of_def:
        if i + 1 == numb:
            print(list_of_def[i])
        i += 1
    if numb == 0:
        break