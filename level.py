from turtle import Turtle

FONT = ('Courier', 24, 'normal')

# other fonts
# 'Arial Black'
# 'Impact'
# 'Verdana'
# Trebuchet MS

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.time_increment = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.display_level()

    def display_level(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", True, align="left", font=FONT)

    def display_game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", True, align="center", font=FONT)
