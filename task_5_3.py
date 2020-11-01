ls_numb = [i for i in range(200,301)]
ls_summ = []
for el in ls_numb:
    i = 1
    summ = 0
    while i < el:
        if el%i == 0:
            summ += i
        i += 1
    ls_summ.append(summ)
i = 0
while i < len(ls_numb):
    z = 0
    while z < len(ls_summ):
        if ls_numb[i] == ls_summ[z] and ls_numb[z] == ls_summ[i]:
            print(ls_numb[i], ls_numb[z])
        z += 1
    i += 1

