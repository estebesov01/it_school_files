class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def print(self):
        print(f'Номер телефона : {self.number}')
        print(f'Модель телефона : {self.model}')
        print(f'Масса телефона : {self.weight}')

    def sendMessage(self,*numbers):
        for i in numbers:
            print('Сообщение отправлено по номеру', i)

iphone_x = Phone('0555555555','iPhone X',135)
redmi = Phone('0777777777','Redmi 8',154)
samsung = Phone('07077077070','Samsung S9',130)
iphone_x.print()
redmi.print()
samsung.print()
redmi.sendMessage('0222222222','0554455445')
