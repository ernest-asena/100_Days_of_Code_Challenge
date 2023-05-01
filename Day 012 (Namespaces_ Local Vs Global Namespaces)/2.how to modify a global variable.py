# If your function has a local variable with same name as global variable and you want to modify the global
# variable inside function then use 'global' keyword before the variable name at start of function i.e.
global total
# It will make the function to refer global variable total whenever accessed. Checkout this example,
total = 100


def func():
    """Modify global variable 'total'"""
    # refer to global variable 'total' inside function
    global total
    if total > 10:
        total = 15


print('Total = ', total)
func()
print('Total = ', total)
