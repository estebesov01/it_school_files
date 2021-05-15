import math, random
def length(sentence):
    i = 0
    count = 0
    while True:
        if sentence[i] != ' ':
            count += 1
        if sentence[i] == sentence[-1]:
            break
        i += 1
    return count

def addDict(first,second):
    first.update(second)
    return first

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

def waiter(food,drink):
    with open('/home/nurs/Рабочий стол/menu.txt','a') as file:
        file.write(food + ' ' + drink + '\n')
    print('Запись прошла успешна.')

def createfile(name):
    with open(f'{name}.txt','w') as file:
        file.write('')


def parent():
    print('Я главная функция')
    child()

def child():
    print('Я вложенная функция')

def tuplemake(somedict):
    keytuple = tuple(somedict.keys())
    valuetuple = tuple(somedict.values())
    return keytuple, valuetuple

def simpleint(n):
    if n < 2:
        print("Число должно быть больше 1")
        quit()
    elif n == 2:
        print("Это простое число")
        quit()
    i = 2 # первый делитель
 
    limit = int(math.sqrt(n))
 
    while i <= limit:
        if n % i == 0:
            print("Это сложное число")
            quit() # выход из программы
        i += 1 # переход к следующему делителю
 
    print("Это простое число")

def makelist(a, b):
    list1 = [a, b]
    return list1

def printNum(num):
    print(str(num) * num)


def nameSalary(name, salary = 5000):
    return f'{name} - {salary}'


def listN(n):
    set1 = set()
    while n != len(set1):
        set1.add(random.randrange(n+20))
    return list(set1)