# Нужно создать класс который принимет модель ноутбука(Acer, Asus, ...) и 
# возвращает полную комплектацию ноутбука со всеми характеристиками.
# В характеристики должны входить:
# 1. Процессор
# 2. Оперативная Память
# 3. Видео карта
# 4. Жёсткий Диск
# 5. Материнская плата
# 6. Размер экрана
# Для каждой характеристики создайте внутри класса функцию которая добавляет по одной характеристики к Dictionary.
# В итоге Ваш класс должен вернуть Dictionary в котором перечислены: 
# Модель Ноутбука и его Характеристики.
class Laptop:
    def __init__(self, name, cpu, ram, graph_card, hdd, screensize):
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.graph_card = graph_card
        self.hdd = hdd
        self.screensize = screensize

    def get_dict(self):
        dict1 = {
            'Название ноутбука':self.name,
            'Процессор':self.cpu,
            'Оперативная память':f'{self.ram} гб',
            'Видеокарта':self.graph_card,
            'Размер диска':self.hdd,
            'Диагональ экрана':self.screensize,
        }
        return dict1
    
    def output(self):
        some_dict = Laptop.get_dict(self).items()
        for k, v in some_dict:
            print(k , ':', v)


my_laptop = Laptop('Acer Aspire 7', 'Intel Core i7', 16, 'nvidia geforce gtx 1650', 512, 15.6)

my_laptop.output()