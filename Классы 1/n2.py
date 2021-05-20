# Нужно создать класс который принимает данные в формате dict. Эти данные, вы сможете взять из Data #1.
# Вам нужно создать 6 методов класса:
# Получить все ключи в TUPLE.
# Получить все значения в TUPLE.
# Получить все ключи в LIST.
# Получить все значения в LIST.
# Получить все ключи в SET.
# Получить все значения в SET.
# Ниже когда вы будете передавать Словарь классу он и вызывать из него любой метод Вы должны получать соответственно нужные типы данных.
# Example: my_class = Parser("DICT") | my_class.get_keys_tuple()
colors = {
    "black": {
    "category": "hue",
    "type": "primary",
    "code": {
    "rgba": [255,255,255,1],
    "hex": "#000"
    }
},
    "white": {
    "category": "value",
    "type": "primary",
    "code": {
    "rgba": [0,0,0,1],
    "hex": "#FFF"
    }
},
    "red": {
    "category": "hue",
    "type": "primary",
    "code": {
    "rgba": [255,0,0,1],
    "hex": "#FF0"
}
},
    "blue": {
    "category": "hue",
    "type": "primary",
    "code": {
    "rgba": [0,0,255,1],
    "hex": "#00F"
}
},
    "yellow": {
    "category": "hue",
    "type": "primary",
    "code": {
    "rgba": [255,255,0,1],
    "hex": "#FF0"
}
},
    "green": {
    "category": "hue",
    "type": "secondary",
    "code": {
    "rgba": [0,255,0,1],
    "hex": "#0F0"
    }
}
}
class Parser:
    def __init__(self,dict1):
        self.dict1 = dict1

    def get_keys_tuple(self):
        inner_keys = list(self.dict1.keys())
        for i in colors:
            inner_keys+=list(self.dict1[i].keys())
            for j in self.dict1[i]:
                try:
                    inner_keys += list(self.dict1[i][j].keys())
                except AttributeError:
                    continue
        return tuple(set(inner_keys))


    def get_values_tuple(self):
        somedict1 = self.dict1.values()
        values = []
        for i in somedict1:
            for j in i.values():
                if type(j) != dict:
                    if j not in values:
                        values.append(j)
                try:
                    values+=list(j.values())
                except AttributeError:
                    continue
        return tuple(values)


    def get_keys_list(self):
        inner_keys = list(self.dict1.keys())
        for i in self.dict1:
            inner_keys+=list(self.dict1[i].keys())
            for j in self.dict1[i]:
                try:
                    inner_keys += list(self.dict1[i][j].keys())
                except AttributeError:
                    continue
        return list(set(inner_keys))


    def get_values_list(self):
        somedict1 = self.dict1.values()
        values = []
        for i in somedict1:
            for j in i.values():
                if type(j) != dict:
                    if j not in values:
                        values.append(j)
                try:
                    values+=list(j.values())
                except AttributeError:
                    continue
        return values


    def get_keys_set(self):
        inner_keys = list(self.dict1.keys())
        for i in self.dict1:
            inner_keys+=list(self.dict1[i].keys())
            for j in self.dict1[i]:
                try:
                    inner_keys += list(self.dict1[i][j].keys())
                except AttributeError:
                    continue
        return set(inner_keys)


    def get_values_set(self):
        somedict1 = self.dict1.values()
        values = []
        for i in somedict1:
            for j in i.values():
                if type(j) != dict:
                    values.append(j)
                try:
                    for q in j.values():
                        if type(q) == list:
                            values.append(tuple(q))
                        else:
                            values.append(q)
                except AttributeError:
                    continue
        return set(values)

my_class = Parser(colors)
data = {
    1:my_class.get_keys_tuple(),
    2:my_class.get_values_tuple(),
    3:my_class.get_keys_list(),
    4:my_class.get_values_list(),
    5:my_class.get_keys_set(),
    6:my_class.get_values_set(),
}
while True:
    print('''1. Ключи в кортеж.
2. Значения в кортеж.
3. Ключи в список.
4. Значения в список.
5. Ключи в множество.
6. Значения в множество.
0. Выход.
    ''')

    id = int(input('Выберите действие - '))
    if id == 0:
        break
    for i in data[id]:
        print(i)