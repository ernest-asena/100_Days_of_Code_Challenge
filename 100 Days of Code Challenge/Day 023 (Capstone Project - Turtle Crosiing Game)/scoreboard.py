from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """This class is responsible for keeping track of the score"""
    def __init__(self):
        """This method initializes the Scoreboard class"""
        super(Scoreboard, self).__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-299, 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", align='left', font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.color('red')
        self.goto(0, 0)
        self.write("CRASHED. GAME OVER!!", align='center', font=FONT)




