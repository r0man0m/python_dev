# Завдання 4

# Створіть програму, яка складається з функції, яка приймає три числа
# і повертає їх середнє арифметичне, і головного циклу, 
# що запитує у користувача числа і обчислює їх середні значення за допомогою створеної функції. 

def average_three_numbers(x = 0, y = 0 ,z = 0):
    sum = x + y + z
    return sum / 3

def main():
    av = 0
    for i in range(3):
        i = int(input('Input value: '))
        av +=average_three_numbers(i)
    print(f'average value = {av}')
main()
    

