#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 

print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? "))

percent_tip = int(input("what percent tip would you like to give? 10, 12 or 15? "))

number_of_people_to_split = int(input("How many people to split the bill? "))

tip = (percent_tip / 100) * total_bill

bill_plus_tip = tip + total_bill

bill_per_person = round((bill_plus_tip / number_of_people_to_split), 2)


print(f"Each person to pay: ${bill_per_person:.2f}")