# Сгенерировать 200 чисел от -100 до 100:
#   1. Каждое число которое делиться на 13 без остатка возводить в квадрат если оно чётное
#   2. Каждое 7 число проверять на НЕчестность и выводить на экран если оно нечётное.
#   3. Посчитать сколько чисел подходят под первое условие
#   4. Посчитать сколько чисел подходят под второе условие
list1 = [i**2 for i in range(-100,100) if i % 2 == 0 and i % 13 == 0 ]
print(list1)
list2 = [i for i in range(-100,100,7) if i % 2 == 1]
print(list2)
print(len(list1))
print(len(list2))