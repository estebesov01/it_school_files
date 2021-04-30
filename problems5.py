#Множество № 1:
dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
#Множество № 2:
farm_1 = {"dog", "cat", "mouse", "sheep"}
#Множество № 3:
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
#1
if 6 in dates_of_birth:
    dates_of_birth.remove(6)
print(dates_of_birth)
#2
set1 = {1,2,3}
set2 = {3,4,5}
set3 = {5,6,7}
set1.union(set2,set3)
print(set1)
#3
print(farm_2-farm_1)
#4
set1 = {1,2,3,4}
set1.add(10)
set1.pop()
print(set1)
#Словарь №1:
menu = {'lagman': 120, 'plov': 120, 'borsh': 100}
#Список № 2
south_american_countries = ['Argentina', 'Bolivia', 
'Brazil', 'Chile', 'Colombia', 'Ecuador', 
'Guyana', 'Paraguay', 'Peru', 'Suriname', 
'Suriname', 'Uruguay', 'Venezuela']
#5
menu['besh_barmak'] = 130
menu['lagman'] = 135
menu.pop('borsh')
print(menu)
#6
drinks = ['Coca-Cola','Sprite','Fanta']
menu['drinks'] = drinks
print(menu)
#7
set_methods = {'add','update','remove','clear','difference','discard',
'intersection','intersection_update','pop'}
dict_methods = {'clear','keys','items','get','values','update'}
#8
log_pass = dict()
for i in range(3):
    login = input("Введите логин : ")
    password = input(("Введите пароль : "))
    log_pass[login] = password
print(log_pass)
#9
names = ['John','Nick','Den']
professions = ['Software Engineer','Manager','Worker']
name_prof = dict()
for i in range(len(names)):
    name_prof[names[i]]=professions[i]
    print(f'Здравствуйте {names[i]}. Прекрасная профессия - {professions[i]}')
#10
set1 = set()
for i in range(10):
    a = int(input("Введите число : "))
    set1.add(a)
set1 = tuple(set1)
print(set1)
#11
south_american_countries = list(set(south_american_countries))
print(south_american_countries)
#12
suitcase = []
for i in range(5):
    v = input("Введите название вещей : ")
    suitcase.append(v)
    if i == 4:
        suitcase.pop(i)
print(suitcase)
#13
print(farm_1&farm_2)
print(farm_1-farm_2)
#14
print(farm_2-farm_1)