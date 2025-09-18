# Завдання 1
# Напишіть програму, яка вводить з клавіатури послідовність чисел, перетворює послідовність на кортеж і 
# виводить його відсортованим у порядку зростання.
my_tuple = ()
sequence_of_numbers = input('Input sequence of numbers: ')
my_tuple = sorted(list(sequence_of_numbers))
for i in my_tuple:
    print(i)
