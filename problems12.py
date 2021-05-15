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
        def __init__(self,dict1) -> None:
            self.dict1 = dict1

        def get_keys_tuple(self):
            inner_keys = list(colors.keys())
            for i in colors:
                inner_keys+=list(colors[i].keys())
                for j in colors[i]:
                    try:
                        inner_keys += list(colors[i][j].keys())
                    except AttributeError:
                        continue
            return set(set(inner_keys))
        def get_values_tuple(self):
            tuple1 = tuple(self.dict1.values())
            return tuple1
        def get_keys_list(self):
            list1 = list(self.dict1.keys())
            return list1
        def get_values_list(self):
            list1 = list(self.dict1.values())
            return list1
        def get_keys_set(self):
            set1 = set(self.dict1.keys())
            return set1
        def get_values_set(self):
            set1 = str(self.dict1.values())
            return set1

    my_class = Parser(colors)

    print(my_class.get_keys_tuple())
    # # print(my_class.get_values_tuple())
    # # print(my_class.get_keys_list())
    # # print(my_class.get_values_list())
    # # print(my_class.get_keys_set())
    # print(my_class.get_values_set())
    #print(colors['green']['code'].keys())

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
        def __init__(self,):
            pass

second()

