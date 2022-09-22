from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-20, 260)
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}", False, "center", FONT)
        self.speed = 0.1

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, "center", FONT)
        self.speed *= 0.9

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", FONT)

