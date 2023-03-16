from turtle import Turtle


class Paddle(Turtle):
    """Paddle definition"""
    def __init__(self, position, color):
        """initialize paddle"""
        super().__init__()
        self.shape('square')
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 60
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 60
        self.goto(self.xcor(), new_y)









