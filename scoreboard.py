from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,260)
        self.write(f"Score: {self.score}", False, align="center",font=('arial',16,'normal'))
        self.hideturtle()
    
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, align="center",font=('arial',16,'normal'))
        
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over Press SPACE to Restart", False, align="center",font=('arial',16,'normal'))


