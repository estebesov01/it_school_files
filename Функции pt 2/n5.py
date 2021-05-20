# Создайте функцию которая принимает 
# слово и создаёт файл с таким именем в 
# той же директории, где был запущен Ваш .py файл.

def createfile(name):
    with open(f'{name}.txt','w') as file:
        pass


name = input('Введите назвние файла : ')
createfile(name)