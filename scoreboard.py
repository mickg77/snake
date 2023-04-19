from turtle import Turtle

class Scoreboard(Turtle) :
    def __init__(self):
        super().__init__() # inheriting the superclass Turtle
        self.goto(-200,270)
        self.score=0
        self.color("white")
        self.updateScoreboard()
        self.hideturtle()

    def updateScoreboard(self):
        self.write(f"Score : {self.score}", align="center", font=("Courier", 20, "normal"))
    def increaseScore(self):
        self.clear()
        self.score+=1
        self.updateScoreboard()

    def gameOver(self):
        self.goto(0,0)
        self.write(f"Game Over : \n You scored {self.score}", align="center", font=("Courier", 20, "normal"))
