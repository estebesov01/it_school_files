# Создайте 2 функции где одна 
# функция вложена в другую. 
# Главная функция должна выводить 
# на экран текст: "Я главная функция". 
# А вложенная функция должна выводить на 
# экран: "Я вложенная функция."
def parent():
    print('Я главная функция')
    child()

def child():
    print('Я вложенная функция')

 
parent()