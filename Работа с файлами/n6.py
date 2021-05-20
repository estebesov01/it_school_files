# Создайте форму регистрации которая спрашивает у 
# пользователя: Логин, Пароль и Фото. Заранее подготовьте 
# фото на компьютере и когда программа спросит ваше фото 
# просто укажите полный путь до места где лежит ваше фото. 
# Программа должна проверить если фото правда существует по 
# такому пути И также это фото с одним из 3 
# расширений("jpeg", "jpg", "png") то вы сохраняете в 
# файл логин, пароль, путь до фото которое указал пользователь. 
# А самому пользователю вы говорите о том что Регистрация Успешна!
while True:
    print('Войдите или зарегистрируйтесь')
    print('1. Регистрация.')
    print('0. Выход.')
    q = input('Выберите действие : ')
    with open('Работа с файлами/textfiles/database2.txt','r') as file:
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
                    with open('Работа с файлами/images/'+photo_path,'rb'):
                        with open('Работа с файлами/textfiles/database2.txt','a') as file:
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
