import statistics
a = 1
b = 0
sum = 0
while(a >=b):
    if(a>=b):
        print('b should by more than a ')
    a = int(input('Input a:'))
    b = int(input('Input b more than a: '))
for i in range(a,b+1):
    if(i%statistics.mean(list(range(a, b+1)))==0):
        sum += i
print(f'Sum of all natural numbers :{sum}')