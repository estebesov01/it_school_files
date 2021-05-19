# Допустим у нас есть список языков программирования. lang1 = 'Rust'
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# Обязательное условие: если переменная в списке, то нужно вывести на экран 
# 'this languages is in list'. 
# Если этого языка нет в списке, ничего не нужно выводить.
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
itlang = input("Введите язык программирования : ")
if itlang in languages:
    print("this languages is in list")
else:
    print('Этого языка нету в списке')