words = ('hello', 'level', 'yesterday')
palindromes = list(filter(lambda word: word == word[::-1], words))
print(palindromes)


