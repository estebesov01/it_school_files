# Есть переменная которая хранит в себе число:
# Необходимо написать следующие условия для проверки переменной:
# 1. Это число трёхзначное?
# 2. Это число положительное и чётное?
# 3. Это число делится на 31 без остатка?
# 4. Если это число больше 100 и оно делится на 17 без остатка или это число больше 150 и равно 13**2 тогда показать что это за число
number = int(input("Введите число : "))
if number > 99 and number < 1000:
    print("Число трёхзначное")
if number > 0 and number % 2 == 0:
    print("Число положительное и чётное")
if number % 31 == 0:
    print("Число делится на 31 без остатка")
if number > 100 and number % 17 == 0 or number > 150 and number == 13**2:
    print(number)