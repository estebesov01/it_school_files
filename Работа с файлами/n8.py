# Возьмите текст #2 и вставьте его в текстовый файл. 
# Возьмите данные из файла и сложите зарплату за Май, 
# Июль, Сентябрь и Ноябрь и посчитайте среднее 
# арифмитечское за эти месяца.
data = dict()
with open('Работа с файлами/textfiles/text2.txt','r') as file:
    for i in file.readlines():
        linedata = i.split()
        data[linedata[0]] = linedata[1]
months = ['May', 'June', 'July','November']
res = 0
for i in months:
    res += int(data[i])
print(res / len(months))