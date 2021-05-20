# Напишите функцию которая генерирует 100 
# рандомных чисел в диапазоне от 10 до 50 и 
# возвращает их в листе. Напишите ДЕКОРАТОР 
# для этой функции которая удалит все дубликаты 
# в первой функции и вернёт всё так же лист.
import random
def decorforlist(func):
    def inner():
        s = set(func())
        return list(s)
    return inner

@decorforlist
def listcreator():
    somelist = [random.randint(10,50) for x in range(100)]
    return somelist
print(listcreator())