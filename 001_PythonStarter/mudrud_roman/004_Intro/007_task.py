isCorrect = False
CORRECT_LOGIN = 'Roman'
CORRECT_PASSWORD = 'Admin'
for i in range(1,4):
    print(f'{i} attempt of authorization ')
    login = input('Input your login: ')
    password = input('Input your password: ')
    if(login==CORRECT_LOGIN and password==CORRECT_PASSWORD and i <=3):
        print(f'Authorization is successful wit  {i} attempt')
        isCorrect = True
    if(isCorrect):
        break
    else:
        print('You are not authorized!')
