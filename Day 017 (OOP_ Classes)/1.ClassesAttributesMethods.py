# In object-oriented programming, a class is a blueprint for creating objects (a particular data structure),
# providing initial values for state (member variables or attributes), and implementations of behavior
# (member functions or methods).
#
# The user-defined objects are created using the class keyword. The class is a blueprint that defines a nature
# of a future object. An instance is a specific object created from a particular class. Classes are used to create and
# manage new objects and support inheritance—a key ingredient in object-oriented programming and a mechanism of reusing
# code. Classes are named with the Pascal Case convention. Others are camelCase and snake_case
# Class attributes are attributes which are owned by the class itself.
# They will be shared by all the instances of the class. Therefore they have the same value for every instance.
# We define class attributes outside all the methods, usually they are placed at the top, right below the class header.

class User:
    pass


user_1 = User
user_1.id = '001'
user_1.name = 'Angela'
print(user_1.name)


# An intuitive way is to create attributes with the constructor method, ie initializing an object os setting starting
# values
# We use the def __init__(self) special function to do this. Here is how:


class Car:
    def __init__(self, model, seats, color):
        self.model = model
        self.seats = seats
        self.color = color


my_mark = Car('Mark X', 5, 'Red')

print(my_mark)


# Adding methods to a class

class Car:
    def __init__(self, model, seats, color):
        self.model = model
        self.seats = seats
        self.color = color

    def enter_race_mode(self, seats):
        self.seats = 2
