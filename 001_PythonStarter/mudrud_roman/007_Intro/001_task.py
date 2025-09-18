# Завдання 1

# Дано два рядки. Виведіть на екран символи, які є в обох рядках.

string_1 = 'abcdefg'
string_2 = 'efghijk'

set_1 = set(string_1)
set_2 = set(string_2)
print(set_1.intersection(set_2))