from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.write(arg=f'Score: {self.score}', font=('Arial', 12, 'normal'), align=ALIGNMENT, move=False)
        self.hideturtle()

    def scoreboard_update(self):
        self.write(f'Score: {self.score}', font=FONT, align='center', move=False)

    def game_over(self):
        self.goto(0, 0)
        self.write('Game over', font=FONT, align='center', move=False)

    def score_increase(self):
        self.score += 1
        self.clear()
        self.scoreboard_update()
