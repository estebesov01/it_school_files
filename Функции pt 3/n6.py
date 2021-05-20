# Напишите функцию которая спрашивает 
# у пользователя login и password. 
# Напишите декоратор который шифрует 
# эти данные и возвращает вам зашифрованные 
# данные. (Можете воспользоваться функцией 
# ord и char, можете загуглить...)
import random
def shifrovka(func):
    def inner():
        alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
        smeshenie = random.randint(0,33)
        message = func().upper()
        itog = ''
        for i in message:
            mesto = alfavit_EU.find(i)
            new_mesto = mesto + smeshenie
            if i in alfavit_EU:
                itog += alfavit_EU[new_mesto]
            else:
                itog += i
        return itog.lower()
    return inner
@shifrovka
def logpass():
    login = input('Введите логин : ')
    password = input('Введите пароль : ')
    return f"{login} - {password}"
print(logpass())
