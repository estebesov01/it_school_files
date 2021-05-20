# Напишите функцию которая спрашивает у 
# вас чтобы вы хотели заказать покушать и 
# выпить. А затем записывает это всё в 
# файл на рабочем столе menu.txt
def waiter(food,drink):
    with open('/home/nurs/Рабочий стол/menu.txt','a') as file:
        file.write(food + ' ' + drink + '\n')
    print('Запись прошла успешна.')


food = input('Введите еду : ')
drink = input('Введите напиток : ')
waiter(food, drink)

