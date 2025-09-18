# Завдання 6

# Створіть прототип програми «Бібліотека», де є можливість перегляду
# та внесення змін за структурою: автор: твір. 
# Передбачте можливість виведення на екран сортування за автором та твором.

from collections import defaultdict
library = defaultdict(list)
action = ''
def start_menu():
    while True:
        print()
        action = input('For add to library the literary work input 1: \n' \
        'For get work from author input 2: \n' \
        'For get literary work from author input 3: \n' \
        'For exit input 4:\n')
        if(action == '1' or action == '2' or action == '3'):
                break
        if(action == '4'):
            print('Exit!')
            break
        else:
            print()
            print('Wrong choice, try again!')
    return action

def add_works():
    cancel = ''
    while True:
        print()
        author = input('Input author: ')
        name_of_work = input('Input name of work: ')
        library[author].append(name_of_work)
        cancel = input('If you have to cancel input - press Enter for continue - press any key and press Enter: ')
        if(cancel == ''):
            return
        
def get_works_with_author():
    cancel = ''
    while True:
        print()
        author = input('Input author: ') 
        print(f'All works {author}: {library.get(author)}')
        print()
        cancel = input('If you have to cancel input - press Enter for continue - press any key and press Enter: ')
        if(cancel == ''):
            return
        
def get_author_with_works():
    while True:
        work = input('Input name of work: ')
        for key, value in library.items():
            if(work in value):
                index_value = value.index(work)
                str_value = value[index_value]
                if(str_value == work):
                    print(f'Author of the work: {key}')
                else:
                    print('Not found the author')
                    continue
            else:
                print('Not found the work')
                break        
        cancel = input('If you have to cancel input - press Enter for continue - press any key and press Enter: ')
        if(cancel == ''):
            return    
        
           

def main():
    while True:
        action = start_menu()
        match action:
            case '1':
                add_works()    
            case '2':
                get_works_with_author()
            case '3':
                get_author_with_works()
            case '4':
                break
main()
