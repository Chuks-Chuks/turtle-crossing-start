from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        new_x = self.xcor()
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(new_x, new_y)

    def finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True

    def starting_point(self):
        self.goto(STARTING_POSITION)
