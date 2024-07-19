from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
            
    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.write('Scoreboard', align='center', font=('Courier', 15, 'bold'))
        self.goto(-100, 230)
        self.write(self.l_score, align='center', font=('Courier', 40, 'bold'))
        self.goto(100, 230)
        self.write(self.r_score, align='center', font=('Courier', 40, 'bold'))
    
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
        
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
        
    def check_winner(self):
        if self.l_score == 10:
            self.goto(0, 0)
            self.write("Left Player Wins!", align='center', font=('Courier', 24, 'bold'))
            return True
        elif self.r_score == 10:
            self.goto(0, 0)
            self.write("Right Player Wins!", align='center', font=('Courier', 24, 'bold'))
            return True
        return False
            
    