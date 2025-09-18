# Завдання 2
# Напишіть програму, в якій користувач вводить із клавіатури діапазон чисел (в діапазоні має бути не менше 5 
# чисел). Вивести на екран суму другого, передостаннього, а також середнього арифметичного значення даної 
# послідовності.

import statistics
list_of_numbers = []
for i in range(1, 6):
    list_of_numbers.append(int(input(f'input {i} number:')))
print(f'sum of second and last but one numbers: {list_of_numbers[1] + list_of_numbers[list_of_numbers.__len__() - 2]}')
print(f'mean of diapason: {statistics.mean(list_of_numbers)}')