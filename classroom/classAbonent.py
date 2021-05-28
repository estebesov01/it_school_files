class Subscriber:

   def __init__(self, subs_id, last_name, first_name,
                mid_name, address, credit_cart_num, debit,
                credit, time_city_out, time_city_in):

       self.subs_id = subs_id
       self.last_name = last_name
       self.first_name = first_name
       self.mid_name = mid_name
       self.address = address
       self.credit_cart_num = credit_cart_num
       self.debit = debit
       self.credit = credit
       self.time_city_out = time_city_out
       self.time_city_in = time_city_in

   def __str__(self):
       return f"{self.last_name} {self.first_name}, {self.subs_id}"


a = Subscriber(1, 'last', 'first', 'mid','address 1', 1234567, 1, 0, 120, 60)
b = Subscriber(2, 'last', 'first', 'mid','address 1', 1234567, 1, 0, 0, 160)
c = Subscriber(3, 'last', 'first', 'mid','address 1', 1234567, 1, 0, 0, 260)
k = Subscriber(4, 'last', 'first', 'mid','address 1', 1234567, 1, 0, 220, 260)

subs_list = [a, b, c, k]

for subs in subs_list:
   if subs.time_city_in >= 200:
       print(subs, 'время городских переговоров превышает заданное')

   if subs.time_city_out > 0:
       print(subs, 'пользовались междугородной связью')