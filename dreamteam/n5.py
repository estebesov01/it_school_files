# import datetime
# date_string = input('ГГГГ-ММ-ДД ЧЧ:ММ :') + ':00'
# format = "%Y-%m-%d %H:%M:%S"
# try:
#     date = datetime.datetime.strptime(date_string, format)
#     print("Формат верный")
# except ValueError:
#     print("Неверный формат")

# list1 = [5,6,7,12,13,14,19,20,21,26,27,28]
# print(date_string[8:10])
# if int(date_string[8:10]) in list1:
#     print('Выходной.')
# else:
import datetime
from datetime import timedelta

def check(d):
    if "05" in d[8:10] or "12" in d[8:10] or "19" in d[8:10] or "26" in d[8:10]:
        print("сейчас это не возможно")
        print(datetime.datetime.now())

d = input("Введите дату:  ")
f = "%Y-%m-%d %H:%M"
add = timedelta(hours=60)

try:
      date = datetime.datetime.strptime(d, f)
      check(d)
      print(f"приходите в {add+date}")
except ValueError:
    print("Неверный формат!")