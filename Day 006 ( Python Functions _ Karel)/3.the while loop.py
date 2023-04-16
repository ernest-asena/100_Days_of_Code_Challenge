# The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.
#
# We generally use this loop when we don't know the number of times to iterate beforehand.

# while test_expression:
#     Body of while

# In the while loop, test expression is checked first.
# The body of the loop is entered only if the test_expression evaluates to True.
# After one iteration, the test expression is checked again.
# This process continues until the test_expression evaluates to False.
#
# In Python, the body of the while loop is determined through indentation.
#
# The body starts with indentation and the first unindented line marks the end.
#
# Python interprets any non-zero value as True. None and 0 are interpreted as False.

# Example 1

number = 1

while number < 10:
    print(f'Current Number is: {number}')
    number += 1

# Example 2
# Program to add natural
# numbers up to
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum_n = 0
i = 1

while i <= n:
    sum_n = sum_n + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum_n)