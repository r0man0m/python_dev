size = int(input('Input size: '))
size = size - size%2
r = size
b = r/2
e = b
for a in range(2):
    if(a == 1):
        r = size
        e = 2
        b = r - 2
        r -= 1
    for i in range(1,r):
        if(i>r/2):
            break
        for y in range(1,r):
            if(y==b or y==e):
                print('*', end=' ')
            else:
                print(' ',end=' ')
        b -= 1
        e += 1
        print()
