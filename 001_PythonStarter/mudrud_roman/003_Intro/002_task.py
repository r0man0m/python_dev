import math
x = float(input(f'Enter  {-round(math.pi, 2)} <= x <= {round(math.pi, 2)}: '))
if(-math.pi <= x <= math.pi):
    print(f'y = {math.floor(math.cos(x))} rad')
else:
    print('x does not match')