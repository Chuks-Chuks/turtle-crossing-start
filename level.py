from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-220, 260)
        self.hideturtle()
        self.level = 1
        self.clear()
        self.write(f"Level:{self.level}", False, "center", ("Courier", 24, "normal"))

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level:{self.level}", False, "center", ("Courier", 24, "normal"))
