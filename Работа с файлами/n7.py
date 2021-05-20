# Напишите программу которая спрашивает от пользователя 2 вещи:
# 1.Путь до картинки которую нужно изменить.
# 2.Путь до картинки НА которую нужно изменить.
# Если оба пути существуют перепишите первую картинку на вторую, 
# если нет скажите пользователю какой картинке не существует.

def checkFormat(filename):
    if ('jpeg' or 'img' or 'png') not in filename:
            raise Exception(f'Формат файла {filename} неправильный')


while True:
    try:
        path_img = input('Введите путь до картинки которую нужно изменить: ')
        checkFormat(path_img)
        path_img_to_change = input('Введите путь до картинки НА которую нужно изменить: ')
        checkFormat(path_img_to_change)
        with open('Работа с файлами/images/' + path_img,'rb') as file:
            r = file.read()
        with open('Работа с файлами/images/' + path_img_to_change,'wb') as file:
            file.write(r)
        break
    except Exception as e:
        print(e)
    except FileNotFoundError:
        print(f'Файл {path_img} не найден')