# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.


print("Welcome to the 'NS007 know your BMI' Program!")
weight = float(input('Let us first get your weight.\nPlease type your weight in kilos here::  '))
height = float(input('Please enter height in cm\nHEIGHT IN CM:: '))

BMI = round(weight / height ** 2)
print(f'Your BMI is {BMI}')
if BMI < 18.5:
    print('You are underweight.')
elif BMI < 25:
    print('You have a normal weight.')
elif BMI < 30:
    print('You are slightly overweight.')
elif BMI < 35:
    print('You are obese.')
else:
    print('You are clinically obese.')


