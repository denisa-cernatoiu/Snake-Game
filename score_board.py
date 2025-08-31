from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 12, 'bold')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(x = 0, y = 280)
        self.color("purple4")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align= ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align= ALIGNMENT, font= FONT)