# You are going to write a program that calculates the sum of all the even numbers from 1 to 100.
# Thus, the first even number would be 2 and the last one is 100:
#
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
#
# Important, there should only be 1 print statement in your console output.
# It should just print the final total and not every step of the calculation.

sum_Evens_zero_to_oneHundred = 0
for number in range(0, 101):
    if number % 2 == 0:
        sum_Evens_zero_to_oneHundred += number

print(f"The sum of the Even Numbers Between 0 and 100 is: {sum_Evens_zero_to_oneHundred}")

print("*********************************************************************")
# Another way is to alter the step size
sum_Evens_zero_to_oneHundred = 0
for number in range(2, 101, 2):
    sum_Evens_zero_to_oneHundred += number

print(f"Total is: {sum_Evens_zero_to_oneHundred}")