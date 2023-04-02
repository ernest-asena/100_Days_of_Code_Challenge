"""
Instructions
Write a program that switches the values stored in the variables a and b.

Your program should work for different inputs. e.g. any value of a and b.
"""

a = input("Enter value for a: ")
b = input("Enter value for b: ")

# Okay i know how to do this one real quick: just tuple unpacking
# a, b = b, a
# print("You entered value " + b + " for a and " + a + " for b.\nNow a is " + a + " and b is " + b)
#But a more tedious approach would be to create a new variable and use it to switch stuff. Something like:

c = a
a = b
b = c 
print("You entered value " + b + " for a and " + a + " for b.\nNow a is " + a + " and b is " + b)


