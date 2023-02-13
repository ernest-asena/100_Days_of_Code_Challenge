# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    """
    basic function example
    """
    print('Hello there!')
    print('Good morning!')
    print('It will be cold today, reaching -3. Wear warm clothing')


greet()


# A function that allows for input
def greet_with_name(name):
    """
    func with parameter example
    """
    print(f'Hello {name}.')
    print('Good morning!')
    print('It will be cold today, reaching -3. Wear warm clothing.')


greet_with_name('Nessi')
