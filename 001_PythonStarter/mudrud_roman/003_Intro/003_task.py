a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
sqr_val = pow((b*b - 4*a*c), 0.5)
if(type(sqr_val) == complex):
    print('No real roots')    
elif(sqr_val == 0):
    print('x = ', (-b) / (2 * a))
else:
    print('x1 = ', ((-b)+ sqr_val )/ (2 * a), '\n', 'x2 = ',((-b) - sqr_val )/ (2 * a))