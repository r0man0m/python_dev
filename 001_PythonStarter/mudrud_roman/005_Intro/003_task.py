# Завдання 1
# Створіть програму, яка зчитує рядок, в якому знаходиться ПІБ користувача і перевіряє, чи складається рядок з 
# літер, при чому кожне слово має бути записане з великої літери. Вивести результат на екран.

name = input('Enter name, surname, middle name: ')
name_tuple =name.split(' ')
for i  in name_tuple:
    if(i.istitle()):
        print(f'{i} With a capital letter')
    else:
        print(f'{i} With a small letter')
    if(i.isalpha()):
        print(f'{i} consists of letters')
    else:
        print(f'{i} consists of not letters')