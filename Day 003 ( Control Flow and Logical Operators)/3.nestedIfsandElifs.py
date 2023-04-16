# an if statement can be contained inside another if statement
# elif statements enable us to evaluate multiple conditions with the if statement

height = int(input('Enter your height in cm.\nHEIGHT::  '))

if height >= 120:
    print('You can ride!')
    age = int(input('Enter your age in numbers.\nAGE::  '))
    if age < 12:
        print('You pay $5.')
    elif 12 <= age <= 18:      # elif age <=18 will also work just fine
        print("You pay $7")
    else:
        print('You pay $12.')
else:
    print('Sorry. You are not tall enough to ride!')