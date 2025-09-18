f = int(input('Input value: '))
result = 1
for i in range(1, f+1):
    result *= i
print(f'Factorial {f}! = {result}')