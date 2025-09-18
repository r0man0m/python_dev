import math
exit = 'Yes'
while(exit != 'No'):
    type_operation = int(input('If you need operation with two arguments enter 2\n'
    'If you need one argument operation enter 1: \n'))
    if(type_operation == 2):
        val_one = float(input('value one: '))
        operand = input('action: ')
        val_two = float(input('value two: '))
        if(operand == '+'):
            print(val_one, '+', val_two, '=', val_one + val_two)
        elif(operand == '-'):
            print(val_one, '-', val_two, '=', val_one - val_two)
        elif(operand == '/'):
            print(val_one, '/', val_two, '=', val_one / val_two)
        elif(operand == '*'):
            print(val_one, '*', val_two, '=', val_one * val_two)
        elif(operand == '**'):
            print(val_one, '**', val_two, '=', math.pow(val_one, val_two))
        else:
            print('Not match operator')
    elif(type_operation == 1): 
        val_one = float(input('value one: '))
        operand = input('action: ')
        if(operand == 'sqrt'):
            print(f' sqrt {val_one} =', math.sqrt(val_one))  
        elif(operand == 'sqrt q'):
            print(f' sqrt  {val_one} =', round(math.pow(val_one, (1 / 3))))
        elif(operand == 'cos'):
            print(f'cos({val_one}) =', math.cos(val_one))
        elif(operand == 'sin'):
            print(f'sin({val_one}) =', math.sin(val_one)) 
        elif(operand == 'tg'):
            print(f'tg({val_one}) =', math.tan(val_one)) 
        else:
            print('Not match operator')   
    exit = input('Continue? Input ''Yes'' or ''No: '' ') 