# Напишите программу которая выводит 
# только нечётные числа с помощью рекурсии.
def zad3(num):
    if num % 2:
        print(num)
    if num > 995:
        return
    zad3(num + 1)
zad3(1)
