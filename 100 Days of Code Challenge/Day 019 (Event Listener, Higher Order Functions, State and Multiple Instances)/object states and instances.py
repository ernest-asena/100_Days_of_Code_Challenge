from turtle import Turtle, Screen
import random

# State is a behavioral design pattern that allows an object to change the behavior when its internal state changes.
# The pattern extracts state-related behaviors into separate state classes and forces the original object to delegate
# the work to an instance of these classes, instead of acting on its own.

# Instance − An individual object of a certain class. An object obj that belongs to a class Circle, for example,
# is an instance of the class Circle. ... Object − A unique instance of a data structure that's defined by its class.
# An object comprises both data members (class variables and instance variables) and methods.

screen = Screen()

is_race_on = False
screen.setup(width=500, height=400)
user_bet= screen.textinput(title='Make your Bet', prompt='Which turtle will win the race?\nCOLOR:::  ')
colors = ['red', 'orange', 'black', 'green', 'blue', 'purple']
all_turtles = []

for i in range(6):

    y=[-180, -110, 0, 50, 100, 180]
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f'CONGRATULATIONS!! YOUR {user_bet} TURTLE WON THE RACE!')
            else:
                print(f'YOU LOSE! The {turtle.pencolor()} Turtle won the Race.')
        random_distance = random.randint(5,10)
        turtle.forward(random_distance)
        turtle.clear()


screen.exitonclick()



