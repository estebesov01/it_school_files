# Создайте текстовый файл с целыми числами -> 
# Найти максимальное и минимальное число и 
# записать в другой файл.
with open('Работа с файлами/textfiles/n9.txt','r') as file:
    a = file.read().split()
sum = 0
for i in a:
    sum += int(i)
print(sum)