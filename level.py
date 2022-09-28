from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-20, 260)
        self.hideturtle()
        self.level = 1
        with open("high_level.txt") as high_level:
            self.highest_level = int(high_level.read())
        self.write_here()

    def level_up(self):
        self.level += 1
        self.write_here()

    def write_here(self):
        self.clear()
        self.write(f"Level:{self.level}  Highest Level: {self.highest_level}", False, "center", FONT)

    def game_over(self):
        if self.level > self.highest_level:
            self.highest_level = self.level
            with open("high_level.txt", mode="w") as high_level:
                self.highest_level = high_level.write(f"{self.highest_level}")
            self.write_here()
        self.level = 1

    def write_game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", FONT)
