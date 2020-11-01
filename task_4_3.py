# с циклом while:
dict_1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
list_of_keys = list(dict_1.keys())
list_of_values = list(dict_1.values())
dict_1_new = {}
i = 0
while i < len(list_of_keys):
    list_of_keys[i] = list_of_keys[i] + str(len(list_of_keys[i]))
    dict_1_new[list_of_keys[i]] = list_of_values[i]
    i += 1
print(dict_1_new)
# с циклом for:
dict_1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for key in dict_1.copy().keys():
    dict_1[key + str(len(key))] = dict_1[key]
    del dict_1[key]
print(dict_1)


