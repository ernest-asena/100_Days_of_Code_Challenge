# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if
# we live until 90 years old.
# There are 365 days in a year, 52 weeks in a year and 12 months in a year.
# Example output: You have 12410 days, 1768 weeks, and 408 months left.

user_age = int(input('Enter your age in years:\n'))
months_left = (90 * 12) - (user_age * 12)
weeks_left = (90 * 52) - (user_age * 52)
days_left = (90 * 365) - (user_age * 365)

print(f'You have {days_left} days, {weeks_left} weeks and {months_left} months.')