#1
while True:
    num = int(input("Введите число : "))
    if num > 0 and num < 10:
        print(num**2)
        break
    else:
        print("Неверное число введите заново в диапазоне от 0 до 10.")
#2
a = int(input("Введите число : "))
b = int(input("Введите число : "))
a, b = b, a
print(a,b)
#3
name = input("Введите имя : ")
surname = input("Введите фамилию : ")
age = int(input("Введите возраст : "))
weight = int(input("Введите вес : "))
if age < 30 and weight > 50 and weight < 120:
    print(name,surname,"Возраст :",age,"вес",weight,"кг хорошее состояние")
elif age > 30 and (weight < 50 or weight > 120):
    print(name,surname,"Возраст :",age,"вес",weight,"кг следует заняться собой")
elif age > 40 and(weight < 50 or weight > 120):
    print(name,surname,"Возраст :",age,"вес",weight,"кг следует обратиться к врачу")