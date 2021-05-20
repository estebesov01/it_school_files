# Возьмите список имён из задания №2 
# и сформируйте 4 разные команды 
# из всех участников.
import random
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
n = int(len(names)/4)
random.shuffle(names)
print(names)
team1 = names[0:n]
team2 = names[n:n*2]
team3 = names[n*2:n*3]
team4 = names[n*3:]
print(team1)
print(team2)
print(team3)
print(team4)