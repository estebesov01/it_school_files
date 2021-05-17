class Student:
    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance

    def getStudentInfo(self):
        return f'{self.name} {self.lastname} поступил в {self.year_of_entrance} г. на факультет:{self.department}.'

me = Student('Нурсултан','Эстебесов','Программная инженерия',2019)
print(me.getStudentInfo())
        
class Airplane:
    def __init__(self, make, model, year, max_speed, odometer):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.is_flying = False

    def take_off(self):
        self.is_flying = True

    def fly(self,distance):
        if self.is_flying == True:
            self.odometer += distance
        else:
            return f'Самолёт еще не взлетел.'


    def land(self):
        self.is_flying = False
        
boeing = Airplane('boeing','777-300',2015,945,134000)
boeing.take_off()
boeing.fly(235)
boeing.land()
print(boeing.odometer)

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70

    def __add_distance(self,distance_km):
        self.odometer += distance_km


    def drive(self,distance_km):
        if self.fuel * 10 > distance_km:
            self.__add_distance(distance_km)
            self.__substract_fuel(distance_km)
            print("Let’s drive!")
        else:
            print('Need more fuel, please, fill')

    def __substract_fuel(self,distance_km):
        self.fuel-=distance_km / 10
        
    
w222 = Car('mercedes','w222','2011')
w222.drive(234)
print(w222.odometer,w222.fuel)
            

    
        