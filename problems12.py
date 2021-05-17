#1
def first():
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
#2
def second():
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

    print('my_class.get_keys_tuple()',my_class.get_keys_tuple())
    print('my_class.get_values_tuple()',my_class.get_values_tuple())
    print('my_class.get_keys_list()',my_class.get_keys_list())
    print('my_class.get_values_list()',my_class.get_values_list())
    print('my_class.get_keys_set()',my_class.get_keys_set())
    print('my_class.get_values_set()',my_class.get_values_set())
    

def third():
    data = {
    "markers": [
    {
    "name": "Rixos The Palm Dubai",
    "position": [25.1212, 55.1535],
    },
    {
    "name": "Shangri-La Hotel",
    "location": [25.2084, 55.2719]
    },
    {
    "name": "Grand Hyatt",
    "location": [25.2285, 55.3273]
    }
    ]
    }
    class Hotels:
        def __init__(self,dict1):
            self.dict1 = dict1


        def getnames(self):
            innerdict = self.dict1.values()
            hotelNames = []
            for i in innerdict:
                for j in i:
                    hotelNames.append(j['name'])
            return hotelNames

        def getNameAndLocationsInDict(self):
            innerdict = self.dict1.values()
            hotelNames = []
            locations = []
            for i in innerdict:
                for j in i:
                    a = list(j.values())
                    for v in range(len(a)):
                        if v % 2 == 0:
                            hotelNames.append(a[v])
                        else:
                            locations.append(a[v])
            hotelDict = {
                'name':hotelNames,
                'location':locations,
            }
            return hotelDict

    hyatt = Hotels(data)
    print(hyatt.getNameAndLocationsInDict())

third()