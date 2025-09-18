# Завдання 5

# Створіть програму, яка приймає як формальні параметри зріст і вагу користувача,
# обчислює індекс маси тіла і в залежності від результату повертає
# інформаційне повідомлення (маса тіла в нормі, недостатня вага або слідкуйте за фігурою).
# Користувач з клавіатури вводить значення росту та маси тіла
# та передає ці дані у вигляді фактичних параметрів під час виклику функції.
# Програма працює доти, доки користувач не зупинить її комбінацією символів «off».

def weight_index(height, weight):
    return weight / pow(height, 2)


def main():
    off = ''
    index = 0
    while True:
        if (off == 'off'):
            print('off')
            break
        else:
            try:
                height = float(input('Input your height: '))
                weight = float(input('Input your weight: '))
                index = weight_index(height, weight)
            except ValueError:
                print('Wrong data!')
                continue
            else:
                if (index <= 18.5):
                    print('Недостатня вага')
                elif (18.5 < index <= 25):
                    print('Маса тіла в нормі')
                elif (25 < index):
                    print('Слідкуйте за фігурою')
                off = input(
                    'For cancel enter "off", for continue press any key: ')


main()
