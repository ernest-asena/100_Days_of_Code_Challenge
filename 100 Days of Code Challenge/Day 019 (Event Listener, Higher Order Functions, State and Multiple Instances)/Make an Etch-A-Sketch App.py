from turtle import Turtle, Screen

tim = Turtle()

def forwards():
    """Move the turtle forward by 10 units"""
    tim.forward(10)
def backwards():
    """moves the turtle backwards by 10 units"""
    tim.backward(10)
def right():
    """turns the turtle right by 10 degrees"""
    tim.right(10)
def left():
    """turns the turtle left by 10 degrees"""
    tim.left(10)
def clear():
    """clears the screen and returns the turtle to the center"""
    tim.clear()
    tim.penup()
    tim.home()

screen = Screen()
screen.listen()
screen.onkey(key='w', fun=forwards)
screen.onkey(key='s', fun=backwards)
screen.onkey(key='a', fun=right)
screen.onkey(key='d', fun=left)
screen.onkey(key='c', fun=clear)
screen.exitonclick()