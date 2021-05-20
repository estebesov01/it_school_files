# Создайте Класс Zoo.
# Инициализируйте класс в объект.
# К объекту Zoo добавьте атрибут animal_1 и присвойте ему значение "Тигр"
# К объекту Zoo добавьте атрибут animal_2 и присвойте ему значение "Бегемот"
# К объекту Zoo добавьте атрибут animal_3 и присвойте ему значение "Жираф"
# В объекте Zoo измените значение атрибута animal_1 и присвойте ему значение "Лев".
# К объекту Zoo добавьте атрибут animal_4 и присвойте ему list состоящий из animal_2 и animal_3
# В объекте Zoo измените значение атрибута animal_3 и присвойте ему значение "Змея".
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