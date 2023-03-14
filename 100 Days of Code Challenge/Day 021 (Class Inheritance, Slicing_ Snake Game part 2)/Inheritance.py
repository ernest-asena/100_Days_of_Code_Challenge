# Inheritance allows us to define a class that inherits all the methods and properties from another class.
#
# Parent class is the class being inherited from, also called base class.
#
# Child class is the class that inherits from another class, also called derived class.

class Animal:
    """Base class for all animals."""
    def __init__(self):
        """Initialize class attributes."""
        self.num_eyes = 2

    def breathe(self):
        """Prints a message about breathing."""
        print('Inhale, Exhale.')


class Fish(Animal):
    """Base class for fish"""
    def __init__(self):
        """initialize class"""
        super().__init__()

    def breathe(self):
        """Override the breathe method from the parent class."""
        super(Fish, self).breathe()
        print('Breathing only under water.')

    def swim(self):
        """Prints a message about swimming."""
        print('Moving in Water.')


nemo = Fish()
nemo.breathe()


# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
    """Base class for all persons."""
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

