# Завдання 3
# Напишіть програму, яка на вхід отримує параметри кольору (в діапазоні від 0 до 255 для кожного кольору) у 
# форматі RGB і виводить на екран кортеж, у якому зберігається колір.

red = hex(int(input('Input RED: ')))
green = hex(int(input('Input GREEN:')))
blue = hex(int(input('BLUE: ')))
color = (red, green, blue)
print(color)