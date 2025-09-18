# Завдання 3

# Створіть програму-калькулятор, яка підтримує наступні операції:
# додавання, віднімання, множення, ділення, зведення в ступінь,
# зведення до квадратного та кубічного коренів. 
# Всі дані повинні вводитися в циклі, доки користувач не вкаже, що хоче завершити виконання програми.
# Кожна операція має бути реалізована у вигляді окремої функції. 
# Функція ділення повинна перевіряти дані на коректність та видавати повідомлення про помилку
# у разі спроби поділу на нуль.

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):
    if(y == 0.0):
        print('Error! Division by zero!')
        return
    else:
        return x / y
    
def my_pow(x, y):
    result = 1
    for i in range(y):
        result *= x
    return result

def square_root(x):
    return pow(x, 0.5)

def cubic_root(x):
    return round(pow(x, 1/3))

def main():
    while True:
        print()
        choice = input('Choice action:\n' \
        '"1" - add two numbers \n' \
        '"2" - subtraction two numbers \n'
        '"3" - multiply two numbers \n'
        '"4" - division two numbers \n' \
        '"5" - to the power of the number \n' \
        '"6" - extract the square root of the number \n' \
        '"7" - extract the cubic root of the number \n' \
        '"8" - for exit \n')
        if(choice == '8'):
            print('Exit!')
            break
        else:
            match choice:
                case '1':
                    print()
                    x = float(input('Input "x": '))
                    y = float(input('Input "y": '))
                    print(f'{x} + {y} = {add(x,y)}')
                case '2':
                    print()
                    x = float(input('Input "x": '))
                    y = float(input('Input "y": '))
                    print(f'{x} - {y} = {sub(x,y)}')
                case '3':
                    print()
                    x = float(input('Input "x": '))
                    y = float(input('Input "y": '))
                    print(f'{x} * {y} = {multiply(x,y)}')
                case '4':
                    print()
                    x = float(input('Input "x": '))
                    y = float(input('Input "y": '))
                    if(division(x,y) != None):
                        print(f'{x} / {y} = {division(x,y)}')
                case '5':
                    print()
                    x = float(input('Input "x": '))
                    y = int(input('Input "y": '))
                    print(f'{x} ^ {y} = {my_pow(x,y)}')
                case '6':
                    print()
                    x = float(input('Input "x": '))
                    print(f'sqr({x}) = {square_root(x)}')
                case '7':
                    print()
                    x = float(input('Input "x": '))
                    print(f'cqr({x}) = {cubic_root(x)}')
                case '8':
                    choice = '8'
                case _:
                    print('Unknown command!')

main()
                
    