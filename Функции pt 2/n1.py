# Создайте 4 функции: add(), substract(), 
# multiply(), divide() которые будут 
# принимать по 2 аргумента и возвращать 
# результат: сложения, вычитания, 
# умножения и деления. 
def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return 'На нуль делить нельзя'
    else:
        return a / b


while True:
    print('''1. Сложение.
2. Вычитание.
3. Умножение.
4. Деление.''')
    a = int(input('Введите число : '))
    b = int(input('Введите число : '))
    ch = int(input('Выберите действие : '))
    if ch == 1:
        print(add(a, b))
    elif ch == 2:
        print(substract(a, b))
    elif ch == 3:
        print(multiply(a, b))
    elif ch == 4:
        print(divide(a, b))
    else:
        print('Неправильный ввод.')