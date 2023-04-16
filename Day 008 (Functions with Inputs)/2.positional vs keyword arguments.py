# Functions with more than one input

def greet_with_name(name, location):
    print(f'Hi {name}.')
    print(f'What is the weather today in {location}?')


# By default, position is in place while assigning arguments to parameters.
greet_with_name('nesi', 'khwisero')

# Here is keyword arguments example
greet_with_name(name='Ernest', location='Los Angeles')
greet_with_name(location='Frankfurt', name='Angele')
greet_with_name(location='Busia', name='Sankara')
