# #1
# ds = '''bin    dev   lib    libx32      mnt   root  snap      sys  var
# boot   etc   lib32  lost+found  opt   run   srv       tmp
# cdrom  home  lib64  media       proc  sbin  swapfile  usr
# '''.split()

# with open('directories.txt','w') as file:
#     for i in ds:
#         file.write(i + '\n')
# with open('directories.txt','r+') as file:
#     print(file.read())

# #2
# login = input("Введите логин : ")
# password = input("Введите пароль : ")

# with open('users.txt','a') as file:
#     file.write(login + ' ' + password + '\n')
# #3
# with open('users.txt','r') as file:
#     if 'w' in file.read():
#         print('Да, в тексте есть w')
#     else:
#         print('Нет, в тексте нет w')

# #4
# t_words = []
# with open('python.txt','r') as file:
#     for i in file.read().split():
#         if ('t' or 'T') in i:
#             t_words.append(i)
#     print('Слова в которых есть буква T : ',', '.join(t_words))
# #5
# while True:
#     print('Войдите или зарегистрируйтесь')
#     print('1. Войти.')
#     print('2. Регистрация.')
#     print('0. Выход.')
#     q = input('Выберите действие : ')
#     with open('database.txt','r') as file:
#             users_db = {}
#             for i in file.readlines():
#                 logpass = i.split()
#                 users_db[logpass[0]] = logpass[1]
#     if q == '1':
#         username = input('Введите логин : ')
#         if username in users_db.keys():
#             for i in range(3):
#                 password = input('Введите пароль : ')
#                 if users_db[username] == password:
#                     print(f'Добро пожаловать, {username}\n')
#                     break
#                 else:
#                     print('Неправильный пароль, кол-во попыток : ',2 - i)
#         else:
#             print('Неправильный логин\n')
#     elif q == '2':
#         while True:
#             username = input('Введите логин : ')
#             if not(username in users_db.keys()):
#                 password = input('Введите пароль : ')
#                 with open('database.txt','a') as file:
#                     file.write(username + ' ' + password + '\n')
#                 print('Вы успешно зарегистрировались\n')
#                 break
#             else:
#                 print('Пользователь с таким логином уже существует')
#     elif q == '0':
#         break
#     else:
#         print('Неправильный ввод\n')
    
#6
while True:
    print('Войдите или зарегистрируйтесь')
    print('1. Регистрация.')
    print('0. Выход.')
    q = input('Выберите действие : ')
    with open('database2.txt','r') as file:
            users_db = {}
            for i in file.readlines():
                logpass = i.split()
                value = []
                value.append(logpass[1])
                value.append(logpass[2])
                users_db[logpass[0]] = value
    if q == '1':
        while True:
            username = input('Введите логин : ')
            if not(username in users_db.keys()):
                password = input('Введите пароль : ')
                photo_path = input('Введите путь к файлу : ')
                try:
                    with open(photo_path,'rb'):
                        with open('database2.txt','a') as file:
                            file.write(username + ' ' + password + ' ' + photo_path + '\n')
                        print('Вы успешно зарегистрировались\n')
                        break
                except FileNotFoundError:
                    print('Файл не найден')
            else:
                print('Пользователь с таким логином уже существует')
    elif q == '0':
        break
    else:
        print('Неправильный ввод\n')
