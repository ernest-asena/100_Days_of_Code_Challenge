# Inheritance allows us to define a class that inherits all the methods and properties from another class.
#
# Parent class is the class being inherited from, also called base class.
#
# Child class is the class that inherits from another class, also called derived class.

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print('Inhale, Exhale.')


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super(Fish, self).breathe()
        print('Breathing only under water.')

    def swim(self):
        print('Moving in Water.')


nemo = Fish()
nemo.breathe()


# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

