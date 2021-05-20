# Создайте database.txt файл с несколькими логинами и 
# паролями. Затем попросите пользователя войти или 
# зарегистрироваться. Спросите его логин и пароль. 
# Если такой логин уже есть скажите ему что логин 
# уже существует и предложите зарегистрироваться 
# спросив пароль. Если такого логина неоказалось 
# среди уже существющих продолжайте регистрацию. 
# Спросите у него Пароль 2 раза и сохраните в в 
# файл datebase.txt только если пароли совпадают.
while True:
    print('Войдите или зарегистрируйтесь')
    print('1. Войти.')
    print('2. Регистрация.')
    print('0. Выход.')
    q = input('Выберите действие : ')
    with open('Работа с файлами/textfiles/database.txt','r') as file:
            users_db = {}
            for i in file.readlines():
                logpass = i.split()
                users_db[logpass[0]] = logpass[1]
    if q == '1':
        username = input('Введите логин : ')
        if username in users_db.keys():
            for i in range(3):
                password = input('Введите пароль : ')
                if users_db[username] == password:
                    print(f'Добро пожаловать, {username}\n')
                    break
                else:
                    print('Неправильный пароль, кол-во попыток : ',2 - i)
        else:
            print('Неправильный логин\n')
    elif q == '2':
        while True:
            username = input('Введите логин : ')
            if not(username in users_db.keys()):
                password = input('Введите пароль : ')
                with open('Работа с файлами/textfiles/database.txt','a') as file:
                    file.write(username + ' ' + password + '\n')
                print('Вы успешно зарегистрировались\n')
                break
            else:
                print('Пользователь с таким логином уже существует')
    elif q == '0':
        break
    else:
        print('Неправильный ввод\n')
    