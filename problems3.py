#1
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
itlang = input("Введите язык программирования : ")
if itlang in languages:
    print("this languages is in list")
#2
for i in languages:
    if i == 'php':
        break
    print(i)
#3
res = 7
for i in range(5):
    res *= 7
    print(res)
#4
n = 0
for i in languages:
    print(n,i)
    n+=1
#5
for i in range(1,11):
    print(i,end=",")
    if i == 10:
        for i in range(9,0,-1):
            print(i,end=',')
#6
names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
n = 0
for i in names:
    if n % 2 == 0:
        print(n,i)
    n+=1
#7
n = 0
for i in names:
    if n % 2 == 1:
        print(n,i)
    n += 1
#8
number = int(input("Введите число : "))
if number > 99 and number < 1000:
    print("Число трёхзначное")
if number > 0 and number % 2 == 0:
    print("Число положительное и чётное")
if number % 31 == 0:
    print("Число делится на 31 без остатка")
if number > 100 and number % 17 == 0 or number > 150 and number == 13**2:
    print(number)
#9
list1 = [i**2 for i in range(-100,100) if i % 2 == 0 and i % 13 == 0 ]
print(list1)
list2 = [i for i in range(-100,100,7) if i % 2 == 1]
print(list2)
print(len(list1))
print(len(list2))