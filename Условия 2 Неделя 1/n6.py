# У нас есть числа от 0 до 100, но не 
# все числа разрешены!
# Разрешенённые:
# От 0 до 21
# От 57 до 100
# Как узнать что какое-то число из 
# запрещёноого диапазона?
num = int(input('Введите число: '))
if num > 0 and num < 21 or num > 57 and num < 100:
    print('Разрешенное число')
else:
    print('Неразрешённое число')