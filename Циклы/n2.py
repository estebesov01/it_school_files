# Будем работать с тем же списком: 
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# С помощью цикла нужно “перебрать” все языки в списке, 
# и когда код доходит до “php”, цикл должен быть прерван.
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
    if i == 'php':
        break
    print(i)