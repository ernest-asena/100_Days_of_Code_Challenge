"""
The Python TypeError is an exception that occurs when the data type of an object in an operation is inappropriate. 
This can happen when an operation is performed on an object of an incorrect type, or it is not supported for the object.
"""

num_char = len(input("What is your name?: "))

new_num_char = str(num_char) # casting

print("Your name has " + num_char + " characters")
 

a = 123
print(type(a))

a = str(123)
print(type(a))

a = float(a)

print(70 + float("100.5"))

print(str(70) + str(100))

