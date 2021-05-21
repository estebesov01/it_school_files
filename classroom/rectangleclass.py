class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getPerimeter(self):
        return (self.length + self.width) * 2

    def getSquare(self):
        return self.length * self.width

    def printRes(self):
        print(f'Периметр прямоугольника с длиной {self.length}см и шириной {self.width}см равен {self.getPerimeter()}')
        print(f'Площадь прямоугольника с длиной {self.length}см и шириной {self.width}см равна {self.getSquare()}')

    def setVal(self,length,width):
        self.length = length
        self.width = width

def inputValues():
    length = int(input('Введите длину : '))
    width = int(input('Введите ширину : '))
    return length, width
while True:
    print('''1. Ввод данных.
2. Вывод результата.
3. Изменение данных.
0. Выход.''')
    q = input('Выберите действие : ')
    if q == '1':
        a, b = inputValues()
        rect = Rectangle(a, b)
    elif q == '2':
        rect.printRes()
    elif q == '3':
        a, b = inputValues()
        rect.setVal(a, b)
    elif q == '0':
        break