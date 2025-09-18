l = int(input('Input length of polygon: '))
h =  int(input('Input height of polygon: ')) - 1
for i in range(1, h+1):
    if(i==1 or i==h):
            for z in range(l):
                print('*', end=' ')
            print()
    for y in range(l):
        if(i==h):
             break
        if(y==0 or y==l-1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()