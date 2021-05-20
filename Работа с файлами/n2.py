# Создайте файл users.txt. Напишите 
# программу которая спрашивает у 
# пользователя его Логин и Пароль 
# и записывает в файл users.txt.
login = input("Введите логин : ")
password = input("Введите пароль : ")

with open('Работа с файлами/textfiles/users.txt','a') as file:
    file.write(login + ' ' + password + '\n')