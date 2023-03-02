from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.color("red")
        self.shape("turtle")
        self.refresh_game()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def level_up(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False

    def refresh_game(self):
        self.goto(STARTING_POSITION)
