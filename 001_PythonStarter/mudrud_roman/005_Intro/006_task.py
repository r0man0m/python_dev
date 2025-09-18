# Завдання 4
# Ознайомтеся за допомогою документації з класами namedtuple та deque модуля collections. Створіть 
# фабрику іменованих кортежів оцінок для учнів однієї групи з предметів: алгебра, геометрія, історія, 
# інформатика, географія. Вивести дані на екран

from collections import namedtuple
from collections import deque

exit = ''
q = deque()
while(exit == ''):
    pupil = namedtuple('Pupil', 'name algebra geometry history informatics geography')

    name = input('Input name of pupil: ')
    algebra = int(input('Input algebra degree: '))
    geometry = int(input('Input geometry degree: '))
    history = int(input('Input history degree: '))
    informatics = int(input('Input informatics degree: '))
    geography = int(input('Input geography degree: '))

    pupil = (name, algebra, geometry, history, informatics, geography)
    q.append(pupil)
    exit = input('Press enter to continue or write something to exit: ')
print(q)





