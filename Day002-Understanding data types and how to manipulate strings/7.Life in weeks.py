# Instructions
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

# https://waitbutwhy.com/2014/05/life-weeks.html

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.

# Hint
# There are 365 days in a year, 52 weeks in a year and 12 months in a year.
# Try copying the example output into your code and replacing the relevant parts so that the sentence is formated the same way.

user_age = int(input("What is your current age?: "))

years_to_90 = 90 - user_age

days_to_live = years_to_90 * 365

weeks_to_live = years_to_90 * 52

months_to_live = years_to_90 * 12

print(f"You have {days_to_live}, {weeks_to_live} and {months_to_live} left.")


