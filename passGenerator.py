import random

def genPass():
    keyboardSpec = '1234567890-_=+qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,<.>/?!@#$%^&*'
    keyboardWOSpec  = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    print('Доступные варианты пароля:\n1. С использованием специальных символов\n2. Без использования специальных символов')
    choise = int(input('Выберите желаемый вариант пароля: '))
    if choise == 1:
        lenPassword = int(input('Введите желаемую длинну пароля: '))
        pasGen = random.sample(keyboardSpec, lenPassword)
        result = ''.join(pasGen)
        print(f'Ваш сгенерированный пароль: {result}')
    elif choise == 2:
        lenPassword = int(input('Введите желаемую длинну пароля: '))
        pasGen = random.sample(keyboardWOSpec, lenPassword)
        result = ''.join(pasGen)
        print(f'Ваш сгенерированный пароль: {result}') 

genPass()