frase = input('frase of 10 symbols: ')
sum = 0
for val in frase:
    sum += ord(val)
print('sum of all symbols: ', sum)