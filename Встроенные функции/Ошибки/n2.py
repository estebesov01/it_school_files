# Спросите у пользователя 5 чисел добавьте их в 
# SET и скажите какое самое маленькое число он ввел.
q = set()
for i in range(5):
    num = int(input("Введите число : "))
    q.add(num)
print(min(q))
