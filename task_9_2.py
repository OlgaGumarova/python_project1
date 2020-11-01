func = lambda **kwargs: kwargs
dict = func(a=2, b=4, c=6)
result = {key*2: value for key, value in dict.items()}
print(result)