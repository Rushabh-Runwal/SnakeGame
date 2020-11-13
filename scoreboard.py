from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 280)
        self.color('#fff')
        self.update()

    def update(self):
        self.write(f'Score = {self.score}', move=False, align="center", font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over.', move=False, align="center", font=("Arial", 14, "normal"))

    def increment(self):
        self.clear()
        self.score += 1
        self.update()
