# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])


# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# Some code for a todo list
# to_doList = []
# to_add = (input('WOULD YOU LIKE TO ADD SOME ITEMS TO YOUR LIST??\nYES/NO?::  ')).lower()
# if to_add == 'y' or to_add == 'yes':
#
#     add_other = True
#     while add_other:
#         print('--------------------------------------------------------------------')
#         item = input('Add A To-Do Item::   ')
#         to_doList.append(item)
#         print(f'You added {item}.')
#         print(f"Your list now has: {to_doList}.")
#
#         ctn = input('Add another?\nYes/No.::  ').lower()
#
#         if ctn == 'n' or ctn == 'no':
#             add_other = False
#         print('You added the following to your list;')
#         print(to_doList, end=' ')
#
#
# else:
#     print('Thank you. Come back later when you have something to add to your list.')
#     print('_____________________________________________________________________')