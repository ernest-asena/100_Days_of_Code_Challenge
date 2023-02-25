# What is a Python dictionary?
# A dictionary is an unordered and mutable Python container that stores mappings of unique keys to values.
# Dictionaries are written with curly brackets ({}), including key-value pairs separated by commas (,).
# A colon (:) separates each key from its value.

programming_dictionary = {
    'bug': 'An error in a dictionary that prevents a program from running as expected.',
    'function': 'A piece of code that you can call over and over again.',
    'loop': 'The action of doing something over and over again,'
}

print(programming_dictionary['bug'])

programming_dictionary['tuple'] = 'A data type in Python that is immutable.'

# creating an empty dictionary
empty_dict = {}
empty_dict2 = dict()

# wipe an entire dictionary
# programming_dictionary = {}

# edit values
programming_dictionary['bug'] = 'A moth in your computer.'

# Looping through dictionaries
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
