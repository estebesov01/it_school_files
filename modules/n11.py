# Определить дату, которая наступит 
# через 1000 дней от текущей даты
import datetime as dt
now = dt.datetime.now()
thousand = dt.timedelta(days=1000)
after = now + thousand
print(after.strftime('%d %B %Y %H:%M:%S'))