# Возьмите код #1 и создайте для него 
# try... except... Создайте несколько 
# except выражений для разных типов ошибок
#Code #1:
try:
    at = 10
    in1 = 15
    wo = 20
    for e in range(-at, at):
        print(wo / e)
    if at > '5':
        print("at > 5")
except ZeroDivisionError:
    print('Делить на ноль нельзя')