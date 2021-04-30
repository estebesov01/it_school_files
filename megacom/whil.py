#1
summ = 0
i = 0
while summ < 1000:
    print(i,summ)
    summ += i
    i+=1
#2
while True:
    num = int(input("Введите число : "))
    if num > 100:
        print("Вы ввели число больше 100")
        break
