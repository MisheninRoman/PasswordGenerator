import random

def genPass():
    keyboard = '1234567890-_=+qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,<.>/?!@#$%^&*'
    pasGen = random.sample(keyboard, 8)
    result = ''.join(pasGen)
    print(f'Ваш сгенерированный пароль: {result}')

genPass()