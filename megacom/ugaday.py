import random
randNum = random.randint(0,100)
for i in range(10):
    print(i,"попытка")
    num = int(input("Угадайте число : "))
    if num == randNum:
        print("Вы угадали.")
        break
    elif num > randNum:
        print("Введенное число больше.")
    else:
        print("Введенное число меньше.")
    if i == 9:
        print("Случайное число =",randNum)
