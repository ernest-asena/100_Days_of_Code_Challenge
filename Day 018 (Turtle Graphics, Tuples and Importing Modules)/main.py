import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
tim.shape('classic')
tim.color('red')
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    my_color = (r, g, b)
    return my_color


# for i in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# def shape_draw(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     shape_draw(shape_side_n)


screen = Screen()
screen.exitonclick()
