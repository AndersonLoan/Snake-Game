from turtle import Turtle
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.goto(0,280) 
    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align="center", font=("white",15,"italic"))


    def earnpoint(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center", font=("white",15,"italic"))
        
        
