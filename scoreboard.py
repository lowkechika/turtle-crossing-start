from turtle import Turtle
FONT = ("Courier", 14, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

    def raise_score(self):
        self.score += 1

    def display_level(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(x=-250, y=270)
        self.write(f"Level: {self.score}", False, font=FONT, align=ALIGN)
