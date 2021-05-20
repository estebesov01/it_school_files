# Создать пустой лист.
# Добавить в него сначала 
# Ваше Имя, Год Рождения, 
# любимый Язык Программирования.
name = input("Введите имя : ")
birthYear = int(input("Введите год рождения : "))
lang = input("Введите любимый язык программирования : ")
list1 = []
list1.append(name)
list1.append(birthYear)
list1.append(lang)
print(list1)