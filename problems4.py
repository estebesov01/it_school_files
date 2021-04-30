#1
someList = [(1,1),(2,2),(3,3),(4,4),(5,5)]
#2
tuple1 = 1,2,3
print(tuple1[0],tuple1[1],tuple1[2])
#3
list1 = [123,123.0,"qwer",bool,[1,2]]
#4
names = ['John','Nick','Tony','Nate','Dustin']
name = ' '.join(names)
print(name)
#5
tuple1 = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)
print(tuple1[:3])
print(tuple1[3:6])
print(tuple1[6:9])
print(tuple1[9:12])
print(tuple1[12:15])
#6
names = ['0Jack', '1Jimmy', '2Jackson', '3Jhon', '4Jackson', '5Jhon',
'6Jimmy', '7Jackson', '8Jhon','9Jack', '10Jimmy',
 '11Jack', '12Jackson', '13Jhon', '14Jackson', 
 '15Jhon','16Jack', '17Jimmy', '18Jack', '19Jackson', '20Jhon',]
print(names.count('Jack'))
#7
i = 0
while i<5:
    if i % 2 == 0:
        names.pop(i)
    if i % 2 == 1:
        names.pop(i)
    i+=1
print(names)
#7.1
i = 0
print(len(names))
names1 = []
while i < len(names):
    if i % 2 == 1 or i > 9:
        names1.append(names[i])
    i+=1
for i in names1:
    print(i)
print(len(names1))
i = 0
#8
name = input("Введите имя : ")
birthYear = int(input("Введите год рождения : "))
lang = input("Введите любимый язык программирования : ")
list1 = []
list1.append(name)
list1.append(birthYear)
list1.append(lang)
print(list1)