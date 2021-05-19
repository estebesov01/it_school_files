def first():
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


def second():
    class Zoo:
        pass
    zoo_object = Zoo()
    zoo_object.animal_1 = 'Тигр'
    zoo_object.animal_2 = 'Бегемот'
    zoo_object.animal_3 = 'Жираф'
    zoo_object.animal_1 = 'Лев'
    zoo_object.animal_4 = [zoo_object.animal_2,zoo_object.animal_3]
    zoo_object.animal_3 = 'Змея'
    print(list(zoo_object.__dict__.values()))
    
second()
11=+2
'1'+'1'