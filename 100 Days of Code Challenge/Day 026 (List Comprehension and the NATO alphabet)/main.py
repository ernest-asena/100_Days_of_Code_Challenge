# List comprehension in Python is an easy and compact syntax for creating a list from a string or another list.
# It is a very concise way to create a new list by performing an operation on each item in the existing list.
# List comprehension is considerably faster than processing a list using the for loop.
# new_list = [new_item for item in list]

numbers = [1, 2, 3, 4]
numbers_add_one = [number + 1 for number in numbers]
print(numbers_add_one)
print('********************************************************')
name = 'Mosh Hamedani'
letters_name = [letter for letter in name if letter != ' ']
print(letters_name)
print('********************************************************')
doubled_numbers = [number * 2 for number in range(1, 5)]
print(doubled_numbers)
print('********************************************************')

# Conditional list comprehensions: we can add a condition. Example;
doubled_numbers = [number * 2 for number in range(0, 5) if number != 0]
print(doubled_numbers)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) <= 4]
long_names = [name for name in names if len(name) > 4]
print('Long names: ', long_names)
print('Short names:', short_names)
long_names_case = [name.upper() for name in names if len(name) > 5]
print(long_names_case)

