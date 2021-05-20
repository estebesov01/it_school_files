# Удалить из Листа №1 все 
# чётные индексы до 10.
names = ['0Jack', '1Jimmy', '2Jackson', '3Jhon', '4Jackson', '5Jhon',
'6Jimmy', '7Jackson', '8Jhon','9Jack', '10Jimmy',
 '11Jack', '12Jackson', '13Jhon', '14Jackson', 
 '15Jhon','16Jack', '17Jimmy', '18Jack', '19Jackson', '20Jhon',]
i = 0
while i<5:
    if i % 2 == 0:
        names.pop(i)
    if i % 2 == 1:
        names.pop(i)
    i+=1
print(names)