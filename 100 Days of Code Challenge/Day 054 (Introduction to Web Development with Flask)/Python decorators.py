# Simple Python Decorator Functions
import time


def delay_decorator(function):
    """A decorator function that delays the execution of another function by 2 seconds"""
    def wrapper_function():
        """A wrapper function that delays the execution of another function by 2 seconds"""
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after

    return wrapper_function


@delay_decorator
def say_hello():
    """A function that prints out 'Hello'"""
    print("Hello")


# With the @ syntactic sugar
@delay_decorator
def say_bye():
    """A function that prints out 'Bye'"""
    print("Bye")


# Without the @ syntactic sugar
def say_greeting():
    """A function that prints out 'How are you?'"""
    print("How are you?")


decorated_function = delay_decorator(say_greeting)
decorated_function()
