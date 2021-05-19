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

