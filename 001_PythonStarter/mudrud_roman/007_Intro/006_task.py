# Завдання 7

# Створіть прототип програми «Облік кадрів», в якій є можливість перегляду та внесення змін до структури
# (реалізуйте інтерфейс(меню), за допомогою якого можна робити маніпуляції з даними):

# прізвище:

#     посада: ...

#     досвід роботи: …

#     портфоліо: …

#     коефіцієнт ефективності: …

#     стек технологій: …

#     зарплата: …

# Передбачте можливість виведення на екран сортування за прізвищем та найефективнішим співробітником.

# name = '', employee_data = dict( position = '', experience = '', portfolio = [], efficiency_ratio = 0, stack_technology = [], salary = 0


# employee_data['Roman'] = dict(position = 'Boss', experience = 'Hi', portfolio = ['Google', 'Amazon'], efficiency_ratio = 100, stack_technology = ['Java', 'Python'], salary = 2500)
def input_lists(input_text):
    value = []
    cancel = ''
    while True:
        if(cancel == 'c'):
            break
        else:
            value.append(input(f'{input_text}: '))
            cancel = input('If you have cancel input enter "c" or press any key: ')
    return value

def set_employee():
    employee_name = input('Input employee name: ')
    employee_data_values = []
    employee_data_keys = list(['position', 'experience', 'portfolio', 'efficiency_ratio', 'stack_technology', 'salary'])
    employee_position = input('Input position: ')
    employee_data_values.append(employee_position)
    employee_experience = input('Input experience: ')
    employee_data_values.append(employee_experience)
    employee_portfolio = input_lists('Input recently job')
    employee_data_values.append(employee_portfolio)
    employee_efficiency_ratio = int(input('Input efficiency ratio: '))
    employee_data_values.append(employee_efficiency_ratio)
    employee_stack_technology = input_lists('Input name of technology')
    employee_data_values.append(employee_stack_technology)
    employee_salary = int(input('Input salary: '))
    employee_data_values.append(employee_salary)
    employee_data_items = list(range(len(employee_data_keys)))
    for i in range(len(employee_data_keys)):
         employee_data_items[i] = list([employee_data_keys[i], employee_data_values[i]])


    employee_dict_list = list([list([employee_name, dict(employee_data_items)])])
    return employee_dict_list

def create_employee(employee_dict):
    cancel = ''
    while True:
        if(cancel == 'c'):
            break
        else:
            employee_dict.update(set_employee())
            cancel = input('Cancel input - input "c" or press any key:  ')
    return employee_dict

def select_employee_data(employee_dict):
    cancel = ''
    while True:
        select = input('For select data all employees input "1":\n\
For select data one employee input "2":\n-> ')
    
def read_all_data(employee_dict):
    key = list(employee_dict.keys())
    value = list(employee_dict.values())
    for i in range(len(key)):
        print(f'{key[i]} {dict(value[i])['position']}')
        

def main():
    employees = dict(Roman = dict(position = 'Jun', experience = 'Low', portfolio = ['Java Rush', 'Zdorove'], efficiency_ratio = 88, stack_technology = ['Java', 'Python'], salary = 1500),
    Vlad = dict(position = 'Middle', experience = 'Hi', portfolio = ['Java', 'Python'], efficiency_ratio = 99, stack_technology = 99, salary = 5000))
    # select_employee_data(employees)
    # create_employee(employees)
    read_all_data(employees)
    
    
    # print(employees)
     
main() 
    
    
    

# employee_name = 'Vasya'
# employee_position = 'Boss'
# employee_experience = 'Hi'
# employee_portfolio = ['Google', 'Amazon']
# employee_efficiency_ratio = 100
# employee_stack_technology = ['Java', 'Python']
# employee_salary = 2500

# employee_data_keys = list(['position', 'experience', 'portfolio', 'efficiency_ratio', 'stack_technology', 'salary'])
# employee_data_values = list([employee_position, employee_experience, employee_portfolio, employee_efficiency_ratio, employee_stack_technology, employee_salary])
# employee_data_items = list(range(len(employee_data_keys)))
# for i in range(len(employee_data_keys)):
#     employee_data_items[i] = list([employee_data_keys[i], employee_data_values[i]])


# employee_dict = dict(list([list([employee_name, dict(employee_data_items)])]))

# print(employee_dict)


 





