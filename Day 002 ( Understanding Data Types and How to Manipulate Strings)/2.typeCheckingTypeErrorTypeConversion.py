num_char = len(input('What is your name: '))

print(type(num_char))

num_char = str(num_char)

print("your name is " + num_char + " characters long.")

a = 123
print(type(a))

a = str(a)
print(type(a))

a = float(a)
print(type(a))

a = bool(a)
print(type(a))

print(70 + float('100.5'))
print(str(70) + str(100))

# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output
# should be 3 + 5 = 8
two_digit_number = input('Enter a two digit number here:\n')
print(f'The result of adding your two digits in {two_digit_number} is:')
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# Another way to do this in small steps could be as follows;
two_digit_number = input('Enter a two digit number here:\n')
digit_one = two_digit_number[0]
digit_two = two_digit_number[1]
result = int(digit_one) + int(digit_two)
print(result)