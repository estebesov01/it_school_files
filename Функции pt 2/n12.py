# Напишите функцию которая спрашивает число N 
# и генерирует вам List состоящий из N разных элементов.
import random
def listN(n):
    set1 = set()
    while n != len(set1):
        set1.add(random.randrange(n+20))
    return list(set1)

n = int(input('Введите число : '))
print(listN(n))