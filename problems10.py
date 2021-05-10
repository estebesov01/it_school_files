#1
import problems10funcs as p
def first():
    while True:
        print('''
        1. Сложение.
        2. Вычитание.
        3. Умножение.
        4. Деление.
        ''')
        a = int(input('Введите число : '))
        b = int(input('Введите число : '))
        ch = int(input('Выберите действие : '))
        if ch == 1:
            print(p.add(a, b))
        elif ch == 2:
            print(p.substract(a, b))
        elif ch == 3:
            print(p.multiply(a, b))
        elif ch == 4:
            print(p.divide(a, b))
        else:
            print('Неправильный ввод.')
#2
def second():
    sentence = input('Введите предложение')
    print('Количество букв в предложении -',p.length(sentence))

#3
def third():
    dict1 = {
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
    }
    dict2 = {
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
    }
    print(p.addDict(dict1, dict2))

#4
def fourth():
    food = input('Введите еду : ')
    drink = input('Введите напиток : ')
    p.waiter(food, drink)

#5
def fifth():
    name = input('Введите назвние файла : ')
    p.createfile(name)

def sixth():
    p.parent()

def seventh():
    somedict = {
        1:'bir',
        2:'eki',
        3:'uch',
    }
    a, b = p.tuplemake(somedict)
    print(a)
    print(b)

def eightth():
    num = int(input('Введите число : '))
    p.simpleint(num)

def nineth():
    a = input('Введите первый аргумент : ')
    b = input('Введите второй аргумент : ')
    print(p.makelist(a, b))

def tenth():
    num = int(input('Введите число : '))
    p.printNum(num)

def eleventh():
    name = input('Введите название работника : ')
    salary = int(input('Введите зарплату : '))
    print(p.nameSalary(name,salary))

def twelth():
    n = int(input('Введите число : '))
    print(p.listN(n))
    
twelth()