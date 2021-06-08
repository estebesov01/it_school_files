class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f'Person name: {self.name}')
        print(f'Person age: {self.age}')

class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        print(f'Student name: {self.name}')
        print(f'Student age: {self.age}')
        print(f'Student section: {self.section}')


P = Person("Tomas Wild", 37)


P.display()


S = Student("Albert", 23 , "Mathematics")

S.displayStudent()