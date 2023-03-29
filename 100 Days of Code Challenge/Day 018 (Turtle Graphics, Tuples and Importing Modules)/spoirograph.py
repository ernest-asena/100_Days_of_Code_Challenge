import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    """Return a random RGB color tuple"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# ########## Challenge 5 - Spirograph ########


def draw_spirograph(size_of_gap):
    """Draws a spirograph with a gap of size_of_gap degrees"""
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)
