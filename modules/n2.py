# Вам дан список имён 
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# и вытащите 4 рандомных имени 
# оттуда и сохраните в другой список.
import random
name = []
i = 0
while True:
    randname = random.choice(names)
    if randname not in name:
        name.append(randname)
        i += 1
    if i == 4:
        break
print(name)