from turtle import Turtle, Screen

# from turtle import *
# color('green', 'blue')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(100)
# timmy.left(30)
# timmy.speed(100)
# my_screen = Screen()
# my_screen.exitonclick()

#
# from prettytable import PrettyTable
#
# table = PrettyTable()
# print(table)
# table.add_column('Team', ['Arsenal', 'Chelsea', 'Man Utd'])
# table.add_column('Points', [33, 21, 28])
# table.align = 'r'
# print(table)

from menu import Menu, MenuItem
from coffeemaker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)

