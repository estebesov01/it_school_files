# Спросите у пользователя имя файла. 
# Создайте функцию которая создаёт 
# файл с именем которое передал пользователь. 
# Присвойте ИМЯ функции к переменной и 
# вызывайте функцию через переменную.
def fileCreator(filename):
    with open(filename,'w') as file:
        pass
    return 'Файл создан'

fileName = 'Функции pt1/files/' + input('Введите название файла: ')
n = fileCreator(fileName)
print(n)