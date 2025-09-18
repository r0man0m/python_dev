# Завдання 2

# Створіть дві функції, що обчислюють значення певних алгебраїчних виразів.
# На екрані виведіть таблицю значень цих функцій від -5 до 5 з кроком 0.5.

def float_range(start, stop, step):
    float_range = []
    value = start
    while value < stop:
        float_range.append(value)
        value += step
    return float_range

def linear_func(my_range):
    print('Function: f(x) = 2x + 3')
    for i in my_range:
        print(f'2*{i} + 3 = {2 * i + 3}')

def quadratic_function(my_range):
    print('Function: f(x)=x^2 - 4x + 4')
    for i in my_range:
        print(f'{i}^2 - 4 * {i} + 4 = {pow(i, 2) - 4 * i + 4}')

linear_func(float_range(-5, 5.5, 0.5))
print()
quadratic_function(float_range(-5, 5.5, 0.5))
