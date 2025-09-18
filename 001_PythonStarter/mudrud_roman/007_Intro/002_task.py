# Завдання 2

# Створіть програму, яка емулює роботу сервісу зі скорочення посилань.
# Повинна бути реалізована можливість введення початкового посилання та короткої назви
# і отримання початкового посилання за її назвою.




message_dict = {'Як справи?': 'Привіт! Як справи? Сподіваюся, твій день проходить чудово!', 
                'зустріч': 'Не забудь про нашу зустріч сьогодні о 18:00. Чекаю на тебе! ',
                'захід сонця': 'Я щойно побачив неймовірний захід сонця! Хотів би, щоб ти теж це бачив/бачила',
                'Гарних вихідних!': 'Гарних вихідних! Відпочивай та набирайся сил. ',
                'думаю': 'Просто хотів/хотіла сказати, що думаю про тебе. '}

cancel = 'no'
while(cancel == 'no'):
    message = input('Input message: ')
    short_message = input('Input short message: ')
    message_dict.update({short_message: message})
    cancel = input('cancel input messages ''yes '' or ' 'no :')
    print()
print(f'list of short messages: {message_dict.keys()}')
print('------------------------------------------------')
choice = int(input('If you read message input ''1''\n if you read short message input ''2: '))
if(choice == 1):
    choice_short_message = input('input short message: ')
    print(f'Your message: {message_dict[choice_short_message]}')
    print('------------------------------------------------')
elif(choice == 2):
    choice_message = input('input message: ')
    print(f'Your short message: {[key for key, value in message_dict.items() if value == choice_message].pop()}')

