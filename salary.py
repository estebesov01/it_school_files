oklad = int(input("Оклад работника : "))
dk = int(input("Количество календарных дней по производственному календарю : "))
df = int(input("Количество фактически отработанных дней : "))
pr = int(input("Премии, надбавки : "))
fine = int(input("Штрафы, удержания : "))
res = (oklad/dk*df+pr)*0.87-fine
print(res)