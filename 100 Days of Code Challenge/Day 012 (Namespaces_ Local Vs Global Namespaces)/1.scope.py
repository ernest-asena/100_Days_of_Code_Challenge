
# Image result for scope in python
# Introduction to Scope in Python. The scope defines the accessibility of the python object.
# To access the particular variable in the code, the scope must be defined as it cannot be accessed from anywhere
# in the program. The particular coding region where variables are visible is known as scope.

# What are the types of scope in Python?
# Image result for scope in python
# You will learn about the four different scopes with the help of examples: local, enclosing, global, and built-in.
# These scopes together form the basis for the LEGB rule used by the Python interpreter when working with variables.

# ################## Scope ####################

enemies = 1


def increase_enemies():
    """increase enemies by 1"""
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
