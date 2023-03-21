import time

# complete the code exercise by printing out the speed it takes to run the `fast_function()` vs the `slow_function()`.

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    """Calculate the speed of a function"""
    def wrapper_function():
        """Print the speed of a function"""
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    """Print the speed of a fast function"""
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    """Print the speed of a slow function"""
    for i in range(100000000):
        i * i


fast_function()
slow_function()