# variables are memory allocations to hold some data
country = input('Enter your country: ')
print(country.upper())
length = len(country)

# variables can be switched
a = 4
b = 5

a,b = b,a

print(a)
print(b)

# another way is to have an intermediate variable to do it
c = a
a = b
b = c

print(a)
print(b)

# when naming variables, use names that make sense and are descriptive

# for example; userName or user_name
# variable names cannot begin with integer values
# we should avoid Python keywords like 'print', 'input' etc
# variables in Python are case sensitive
# mistyping variables when calling them causes a name error
