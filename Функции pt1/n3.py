# Создайте функцию сложения, затем 
# функцию вычитания двух чисел...
# Создайте 3-ю функцию которая 
# вызывает первые 2 внутри себя.
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def main():
    a = int(input('Введите число : '))
    b = int(input('Введите число : '))
    print(f'{a} + {b} =',plus(a,b))
    print(f'{a} - {b} =',minus(a,b))
main()