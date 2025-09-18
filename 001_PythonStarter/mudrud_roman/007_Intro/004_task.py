# Завдання 5

# Є рядок, в якому зберігаються 1000 слів. 
# Створіть словник із ключами - унікальними словами та 
# значеннями - кількістю повторів кожного слова у послідовності.
from collections import defaultdict

with open('lesson_7/text.txt', 'r') as file:
    file.seek(0)
    text_list = list(file.read().lower().split())
    text_set = set(text_list)
    text_dict = defaultdict(list)
    for i  in text_set:
        text_dict[i].append(text_list.count(i))
    print(text_dict)