# Instructions
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

height = float(input("Enter heoght in meters:: "))

weight = float(input("Enter weight in kilograms:: "))

BMI = round(weight / (height ** 2))

if BMI < 18.5:
    print(f"BMI: {BMI}. You are underweight.")
elif BMI < 25:
    print(f"BMI: {BMI}. You have a normal weight.")
elif BMI < 30:
    print(f"BMI: {BMI}. You are slightly overweight.")
elif BMI < 35:
    print(f"BMI: {BMI}. You are obese.")
else:
    print(f"BMI: {BMI} You are clinically obese.")
