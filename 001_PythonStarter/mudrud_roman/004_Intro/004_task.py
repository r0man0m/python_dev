size = int(input('Input size: '))
for i in range(size):    
    for y in range(size): 
        if(y == i or y == 0):
            print('*', end=' ')
        elif (i == size - 1):
              print('*', end=' ') 
        else:
                print(' ',end=' ')
    print()               
    