from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 14, 'normal'))

    def add_score_point(self):
        self.score += 1
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=('Arial', 14, 'normal'))
