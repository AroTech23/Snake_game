from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open ( "data.txt" ) as file:
            content = int ( file.read () )
        self.score=0
        self.color ( "white" )
        self.penup()
        self.hideturtle()
        self.goto ( 0 , 278 )
        self.write(f"Score: {self.score}",align="center",font=("Arial",18,"normal"))
    def update_score(self):
        self.clear()
        self.write ( f"Score: {self.score}" , align="center" , font=("Arial" , 18 , "normal") )
    def increase_score(self):
        self.score += 1
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write ( f"GAME OVER" , align="center" , font=("Arial" , 18 , "normal") )




