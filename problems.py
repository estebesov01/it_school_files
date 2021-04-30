#1
print("1")
a = 2**3
b = 3**2
if a > b:
    print("a > b")
elif a == b:
    print("a == b")
else:
    print("b > a")
#2
print("2")
a = 1
b = 2
c = 2
if a >= b and a >= c:
    print("a")
elif b >= a and b >= c:
    print("b")
else:
    print("c")
if a <= b and a <= c:
    print("a")
elif b <= a and b <= c:
    print("b")
else:
    print("c")
#3
print("3")
a = 17391 % 17
b = 546 % 17
c = 934 % 17
if a <= b and a <= c:
    print("a")
elif b <= a and b <= c:
    print("b")
else:
    print("c")
#4
print("4")
x = 13
if x**2 < 172:
    print(x**2**2)
else:
    print("good")
#5
print("5")
a = 5
if a % 2 == 0:
    print("Четное число")
else:
    print("Нечетное число")
if a % 3 == 0:
    print("Делится на 3")
if a**2 > 1000:
    print("Больше 1000")
else:
    print("Меньше")
#6
print("6")
if True:
    print("Срабатывает в любом случае.")
if True:
    if True:
        if True:
            pass
        else:
            pass
    else:
        pass
else:
    pass
#7
print("7")
a = 10//5
b = 10/5
if a == b:
    print("Равны",a+b)
else:
    print("Не равны.")
#8
print("8")
a = -15
if a < 0:
    print(a)
else:
    print("Число положительное")
#9
print("9")
a = 10
b = 5
if a > 0 and b > 0:
    print("Они положительные")
#10
print("10")
if a > b:
    print(a+2)
else:
    print(b+2)