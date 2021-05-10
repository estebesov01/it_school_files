import my_module, random, sys, fileinput, os
#1
print(my_module)


#2
names = ["Aibek", "Joomart", "Adinai", 
"Ermek", "Atai", "Aslan", 
"Lyazat", "Salavat", "Daniyar", 
"Bolotbek", "Alymbek", "Dastan", 
"Maksat"]
name = []
for i in range(4):
    name.append(random.choice(names))
print(name)


#3
print(sys.platform)


#4
# for line in sys.stdin:
#     print(line)

import sys
sys.stderr.write('qwe')
sys.stderr.flush()
print(sys.argv)
#5
# os.mkdir('/home/nurs/Рабочий стол/some_dir/')
# for i in range(5):
#     with open(f'/home/nurs/Рабочий стол/some_dir/text_file' + str(random.randint(1, 1234)) + '.txt','w') as file:
#         file.write(str(i))


#6
team1 = []
team2 = []
team3 = []
team4 = []
for i in range(len(names)):
    team1.append(i)
    team2