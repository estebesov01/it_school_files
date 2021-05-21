class Person:
    def __init__(self, fullName, place, age = 18):
        self.fullName = fullName
        self.age = age
        self.place = place

    def move(self,place):
        self.place = place

    def talk(self):
        print(f'{self.fullName} говорит.')

    def __str__(self):
        return f'{self.fullName} в городе {self.place} возраст: {self.age}'

me = Person('Estebesov Nursultan','Bishkek',20)
me.talk()
me.move('Kara-Kul')
print(str(me))