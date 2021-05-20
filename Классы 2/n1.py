# Создайте класс Factory и внутри создайте 2 метода:
# Метод engine который возвращает строку "Двигатель создан"
# Метод bridge который возвращает строку "Ходовая часть создана"
# Создайте класс Toyota который будет НАСЛЕДОВАТЬ класс Factory. 
# В классе Toyota создайте методы wheels и windows.
# Метод wheels возвращает строку "Колёса готовы"
# Метод windows возвращает строку "Стёкла готовы"
# Из класса Toyota вызовите все методы, методы вернут вам строки(объекты)
# Результат каждого метода вставьте в лист
class Factory:
    def engine(self):
        return 'Двигатель создан'


    def bridge(self):
        return 'Ходовая часть создана'


class Toyota(Factory):
    def wheels(self):
        return 'Колёса готовы'

    def windows(self):
        return 'Стёкла готовы'

camry = Toyota()
list_method = [camry.wheels(),camry.windows(),camry.engine(),camry.bridge()]
print(list_method)

