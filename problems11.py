#1
import datetime, random

def first():
    zad1 = lambda h, w, d:f'Объем бассейна {h * w * d} м^3'
    print(zad1(2,3,4))
#2
def second():
    zad2 = lambda d:365 - d
    print(zad2(30))

def third():
    def zad3(num):
        if num % 2:
            print(num)
        num += 1
        if num > 996:
            return
        zad3(num)
    zad3(1)


#4
def fourth():
    set1 = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    def zad4(someset):
        if len(someset) > 0:
            someset.pop()
            zad4(someset)
        else:
            print('Множество очищено')
            return
    zad4(set1)

#5
def fifth():
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
#6
def sixth():
    def shifrovka(func):
        def inner():
            alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
            smeshenie = random.randint(0,33)
            message = func().upper()
            itog = ''
            for i in message:
                mesto = alfavit_EU.find(i)
                new_mesto = mesto + smeshenie
                if i in alfavit_EU:
                    itog += alfavit_EU[new_mesto]
                else:
                    itog += i
            return itog.lower()
        return inner
    @shifrovka
    def logpass():
        login = input('Введите логин : ')
        password = input('Введите пароль : ')
        return f"{login} - {password}"
    print(logpass())


#7
def seventh():
    list1 = [1745345,98726,439872634,7312,64872,123687126,9312,4124,231,3123,34,3453]
    somelambda = lambda x:x * 1.185
    for i in list1:
        somelambda(list1)
    print(list1)

def second1():
    ss = (datetime.datetime.now() - datetime.datetime(2021,1,1))
    zad2 = lambda d:datetime.datetime(2022,1,1) - (datetime.timedelta(days = d) + datetime.datetime(2021,1,1))
    print(zad2())
    print(ss)
sixth()