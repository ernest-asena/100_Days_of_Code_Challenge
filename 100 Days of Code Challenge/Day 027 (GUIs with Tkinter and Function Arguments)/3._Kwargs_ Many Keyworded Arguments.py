# The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument
# list. We use the name kwargs with the double star. The reason is because the double star allows us to pass through
# keyword arguments (and any number of them).

def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        # self.make = kw['make']
        self.model = kw.get('model')
        # or self.model = kw['model']
        # the benefit of get is that it won't throw an error when it does not find a value; returns none
        self.color = kw.get('color')
        self.seats = kw.get('seats')


my_car = Car(make='Nissan')
print(my_car.model)
print(my_car.make)