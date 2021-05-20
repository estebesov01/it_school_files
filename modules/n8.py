# Создайте программу которая спрашивает 
# у пользователя число N для генерации 
# пароля а затем генерирует ему пароль 
# длиною N символов.
import random
pas = ''
n = int(input('Введите количество символов: '))
for x in range(n):
    pas += random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')) 
print(pas)