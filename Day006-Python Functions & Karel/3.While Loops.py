# In Python, a while loop is used to repeatedly execute a block of code until a certain condition is no longer true.
# The basic syntax for a while loop in Python is:

# while condition:
# code to execute while the condition is true

# The condition is a Boolean expression that is evaluated at the beginning of each loop iteration. If the condition
# is True, the code block under the while statement will be executed. This process continues until the condition is
# False.


# Here is an example of a while loop that prints the numbers from 0 to 9:


i = 0
while i < 10:
    print(i)
    i += 1

# In this example, the loop continues as long as the variable i is less than 10.
# During each iteration of the loop, the value of i is printed to the console, and then i is incremented by 1.
# Once i reaches 10, the condition i < 10 becomes False, and the loop ends.


# It's important to note that if the condition in a while loop is never False, the loop will continue to execute
# indefinitely, which can cause your program to crash or become unresponsive. So, it's important to ensure that your
# while loop has a way to eventually terminate.
