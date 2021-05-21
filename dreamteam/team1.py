#1.1
f = 10
r = 10.5
j = 13.7
if r > j:
    print('r > j')
elif r < j:
    print('r < j')
else:
    print('r равно j')
#1.2
a = 4
b = 7.0
if a % 2 == 0:
    print('Число чётное')
elif a % 2 == 1 and a < 4:
    print('Число простое')
print(f'Число {a} положительное или простое')
#1.3
a = 123
b = 321
halfsum = (a + b) / 2
if (a + b) % 2 == 0:
    print(halfsum)
if halfsum < b and halfsum > a:
    print('b > sum/2 > a')
#1.4
a = 35
b = 25
c = 75
if a >= b and a >= c:
    print('max =', a)
    if b >= c:
        print('min',c)
    else:
        print('min =',b)
elif b >= a and b >= c:
    print('max =',b)
    if a >= c:
        print('min =',c)
    else:
        print('min =',a)
elif c >= a and c >= b:
    print('max =',c)
    if a >= b:
        print('min =',b)
    else:
        print('min =',a)
#2.1
summ = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        summ+=i
print('sum =',summ)
#2.2
a = 333
b = 555
a, b = b, a
print(a, b)
#2.3
num = '4729461084'
num = int(num)
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
print("Сумма цифр числа равна: ", sum)
#2.4
date1 = input('Задайте дату в формате "гггг-мм-дд чч:мм" ')
date = dict()
date1 = date1.replace('-', ' ')
date1 = date1.replace(':', ' ')
date1 = date1.split()
keys = ['year','month','day','hours','minutes']
for i in range(5):
    date[keys[i]] = date1[i]
print(date)
#2.5
a = '1'
a = int(a)
print(a+a+a+a+a)
print(a*7)
#2.6
# mkdir -p несуществующая_директория/новая_директория
#2.7
# /home/'developer'/Desktop