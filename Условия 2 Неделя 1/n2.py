# Создайте условие 
# которое определит 
# самое большое и 
# самое маленькое 
# число из трёх.
a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))
if a >= b and a >= c:
    print('max - ',a)
    if b >= c:
        print('min - ',c)
    else:
        print('min - ',b)
elif b >= a and b >= c:
    print('max - ', a)
    if a >= c:
        print('min - ',c)
    else:
        print('min - ',a)
elif c >= a and c >= b:
    print('max - ', c)
    if a >= b:
        print('min - ',b)
    else:
        print('min - ',a)