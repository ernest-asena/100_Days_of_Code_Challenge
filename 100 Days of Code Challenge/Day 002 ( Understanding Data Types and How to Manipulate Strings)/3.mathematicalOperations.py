# We have seen the addition with '+'

# Subtraction with '-'
7 - 4

# Multiplication with '*'
7 * 5

# Division(always returns a float) '/'
6/3

# to the power of(exponential) '**'
6**2

# Order of operations in here can be stated as: PEMDAS
# Parentheses; Exponents; Multiplication; Division; Addition; Subtraction

print(3*3+3/3-3)

# there are more operations or operators than these but these are the basic ones

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a
# short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
weight = input('What is your weight in kilos:\n ')
height = float(input('What is your height in meters:\n '))

weight = int(weight)
height = height**2

# height = height*height
# height = float(height) * float( height)

BMI = round(weight/height)
# BMI = round((weight/height),3) to print it in like 3 dp
print(BMI)

# Here is a short hand way to do this
# print('*********************')
# bmi = int(weight)/float(height**2)
# print(bmi)