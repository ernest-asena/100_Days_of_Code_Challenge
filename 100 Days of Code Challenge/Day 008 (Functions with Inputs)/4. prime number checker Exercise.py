# Prime numbers are numbers that can only be cleanly divided by itself and 1.
#
# https://en.wikipedia.org/wiki/Prime_number
#
# You need to write a function that checks whether if the number passed into it is a prime number or not.
#
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
#
# But 4 is not a prime number because you can divide it by 1, 2 or 4.
#
# https://cdn.fs.teachablecdn.com/s0gceS97QD6MP5RUT49H
#
# Here are the numbers up to 100, prime numbers are highlighted in yellow:

checks = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []


def prime_number_check(number):
    for i in checks:
        if number % i == 0:
            result.append(number)
    if len(result) > 2:
        print(f'Number {number} is not prime.')
    else:
        print(f'Number {number} is prime.')


number = int(input('What is your number?\nNUMBER:: '))
prime_number_check(number)

print('######################################################################')


def prime_checker_2(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f'{number}. A prime number.')
    else:
        print(f'{number}. Not a prime number.')

prime_checker_2(number)