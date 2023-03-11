# A function is called Higher Order Function if it contains other functions as a parameter or returns a function as
# an output i.e, the functions that operate with another function are known as Higher order Functions.

from turtle import Turtle, Screen

tim = Turtle()


def move_forward():
    """Moves the turtle forward by 10 units"""
    tim.forward(10)


def turn_right():
    """Turns the turtle right by 45 degrees"""
    tim.right(45)


screen = Screen()

screen.listen()
screen.onkey(key='space', fun=move_forward)
screen.onkey(key='Left', fun=turn_right)
screen.exitonclick()
