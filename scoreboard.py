from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open ( "data.txt" ) as file:
            content = int ( file.read () )
        self.score=0
        self.highscore = content
        self.color ( "white" )
        self.penup()
        self.hideturtle()
        self.goto ( 0 , 278 )
        self.update_score()
    def update_score(self):
        self.clear()
        self.write ( f"Score: {self.score}  High Score:{self.highscore}" , align="center" , font=("Arial" , 20 , "normal") )
    def increase_score(self):
        self.score += 1
        self.update_score()
    def reset(self):

        if self.score > self.highscore:
            self.highscore = self.score
            with open ( "data.txt",mode="w" ) as name:
                name.write(str(self.highscore))

        self.score=0
        self.update_score()




