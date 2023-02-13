# the range function; gives a range of numbers to loop through
# example:

for number in range(1, 11):
    print(f'Curent number : {number}')

print('***********************************************************************')
# you can configure the step value as follows:
for number in range(1, 11, 4):
    print(f'Curent number is:: {number}')

# add up all the numbers between 1 and 100
sum_one_to_oneHundred = 0
for number in range(0, 101):
    sum_one_to_oneHundred += number

print(sum_one_to_oneHundred)
