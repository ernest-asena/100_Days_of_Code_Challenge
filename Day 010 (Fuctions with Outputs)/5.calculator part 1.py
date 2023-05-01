from calcart import logo


def add(n1, n2):
    """This function adds two numbers together."""
    return n1 + n2


def subtract(n1, n2):
    """This function subtracts two numbers from each other."""
    return n1 - n2


def divide(n1, n2):
    """This function divides two numbers."""
    return n1 / n2


def multiply(n1, n2):
    """This function multiplies two numbers."""
    return n1 * n2


# Create a dictionary of operations

operations = {'+': add,
              '-': subtract,
              '*': multiply,
              '/': divide
              }
print(logo)
print("Welcome to the NS007 Calculator!")


def calculator():
    """This function is the calculator."""
    num1 = float(input('What is the first number?\nFIRST NUMBER:::   '))
    calc_again = True
    while calc_again:
        for symbol in operations:
            print(symbol)
        operator = input('Pick an operator from the list above.\nOPERATOR:::   ')
        num2 = float(input('What is the second number?\nSECOND NUMBER:::   '))

        # if operator == '+':
        #     result = add(num1, num2)
        # elif operator == '-':
        #     result = subtract(num1, num2)
        # elif operator == '*':
        #     result = multiply(num1, num2)
        # elif operator == '/':
        #     result = divide(num1, num2)
        # else:
        #     print('SORRY. INVALID OPERATION.')

        calculation_function = operations[operator]
        result = calculation_function(num1, num2)

        print(
            f"The result of {num1} {operator} {num2} is {result}.\nTHANK YOU FOR USING THE NS007 CALCULATOR.\nGOODBYE!")
        ctn = input(f"Would you like to continue calculating with {result} or would would you like to start over?"
                    f"Maybe you want to exit as well?\nType y to continue calculation with {result}.\nType ctn to "
                    f"start over. "
                    f"\nType n to exit.")
        if ctn == 'y':
            num1 = result
        elif ctn == 'ctn':
            calculator()

        elif ctn == 'n':
            calc_again = False


calculator()
