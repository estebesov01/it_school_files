# Напишите программу которая определяет 
# ПРОСТЫЕ ЧИСЛА. Простое число - это число 
# которое делится только на себя и на 1.
import math
def simpleint(n):
    if n < 2:
        print("Число должно быть больше 1")
        quit()
    elif n == 2:
        print("Это простое число")
        return
    i = 2 
    limit = int(math.sqrt(n))
    while i <= limit:
        if n % i == 0:
            print("Это сложное число")
            return 
        i += 1
    print("Это простое число")


num = int(input('Введите число : '))
simpleint(num)