# The special syntax *args in function definitions in python is used to pass a variable number of arguments to a
# function. It is used to pass a non-key worded, variable-length argument list. The syntax is to use the symbol * to
# take in a variable number of arguments; by convention, it is often used with the word args.

# Unlimited Arguments
# def add(*args):
#     for n in args:
#         print(n)

def add(*args):
    sum_n = 0
    for n in args:
        sum_n += n
    return sum_n


print(add(1, 2, 3, 4, 5, 5))
