# Используя функцию randrange() получите 
# псевдослучайное четное число в пределах 
# от 6 до 12. Также получите число кратное 
# пяти в пределах от 5 до 100.
from random import randrange
n = randrange(6,12)
n2 = randrange(5,100)
while True:
    if n2 % 5 == 0:
        break
    n2 = randrange(5,100)
print(n,n2)