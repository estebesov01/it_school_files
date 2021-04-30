while True:
    a = int(input("Введите число : "))
    b = int(input("Введите число : "))
    znak = input("Введите знак : ").strip()
    if znak == '+':
        print(f'{a} + {b} = {a+b}')
    elif znak == '-':
        print(f'{a} - {b} = {a-b}')
    elif znak == '/':
        if b == 0:
            print("Нельзя делить на ноль")
            continue
        print(f'{a} / {b} = {a/b}')
    elif znak == '*':
        print(f'{a} * {b} = {a*b}')
    elif znak == '0':
        break
    else:
        print("Неправильный знак.")