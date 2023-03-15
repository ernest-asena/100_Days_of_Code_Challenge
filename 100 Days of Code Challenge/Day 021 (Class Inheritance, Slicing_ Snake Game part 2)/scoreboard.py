from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    """Scoreboard class."""
    def __init__(self):
        """Initialize scoreboard."""
        super().__init__()
        self.score = 0
        with open('highscore.txt') as h_score:
            self.high_score = int(h_score.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('highscore.txt', mode='w') as h_score:
                h_score.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
