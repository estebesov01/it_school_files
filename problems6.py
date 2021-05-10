#1
q = ['fa 123213',1,2,3,1,2,'2','1']
w = []
for i in q:
    try:
        set(i)
        w.append(True)
    except TypeError:
        w.append(False)
print(all(w))
#2
q = set()
for i in range(5):
    num = int(input("Введите число : "))
    q.add(num)
print(min(q))
#3
functions = ['all','any','abs','min','eval','reversed',
            'max','slice','round',]
func = input("Введите функцию : ")
if func in functions:
    print('Такая функция есть')
else:
    print('Такой функции нету')
#4
a = 1_234_123_123_565
print(a)