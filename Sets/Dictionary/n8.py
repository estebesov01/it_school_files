# Создайте Dictionary с 5 элементами где ключи это их имена, а значение их профессия.
# С помощь цикла for пройти вывести на экран строку:
# "Здравствуйте <Имя>  Прекрасная профессия <Профессия>"
names = ['John','Nick','Den','Sam','Mark']
professions = ['Software Engineer','Manager','Worker','Teacher','Fireman']
name_prof = dict()
for i in range(len(names)):
    name_prof[names[i]]=professions[i]
    print(f'Здравствуйте {names[i]}. Прекрасная профессия - {professions[i]}')