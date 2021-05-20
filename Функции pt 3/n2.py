# Написать lambda которая получает 
# сколько дней ПРОШЛО с нового года 
# как параметр и говорит пользователю 
# сколько дней ОСТАЛОСЬ до нового года.
import datetime 
now = datetime.datetime.now() - datetime.datetime(2021,1,1)
days = int(str(now).split()[0])
zad2 = lambda d:365 - d
print(f'Сколько дней осталось до НГ:',zad2(days))