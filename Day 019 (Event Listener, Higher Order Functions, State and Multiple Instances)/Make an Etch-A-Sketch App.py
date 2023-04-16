from turtle import Turtle, Screen

tim = Turtle()

def forwards():
    tim.forward(10)
def backwards():
    tim.backward(10)
def right():
    tim.right(10)
def left():
    tim.left(10)
def clear():
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