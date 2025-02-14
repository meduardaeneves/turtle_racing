from turtle import Turtle
import random

FONT_STYLE = ('Arial',15,'bold')
ALIGN = 'center'


class TurtleGameClass(Turtle):
    
    move_or_stay = [x for x in range(0,11)]
    
    def __init__(self,color_chosen,start_x,start_y,total_lengh):
        self.object = Turtle()
        self.color_chosen = color_chosen
        self.start_x = start_x
        self.start_y = start_y
        self.total_lengh = total_lengh
        self.object.color(self.color_chosen) 
        self.object.shape('turtle')    
        self.object.penup()   
        self.object.speed(0)   
        self.object.goto(self.start_x,self.start_y)
        self.total_movement = 0
    
    def move_or_stay_action(self):
        choice_movement = random.randint(0,10)
        self.object.forward(choice_movement)
        self.total_movement += choice_movement
        if self.total_movement >= (self.total_lengh - 20):
            return True
        else:
            return False

class ResultGame(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('black')
    
    def write_winning_paddle_name(self,winng_paddle,your_paddle):
        self.goto(0,0)
        if winng_paddle == your_paddle:
            text = f'YOU WIN!\nThe winning turtle was "{winng_paddle}"'
        else:
            text = f'YOU LOST!\nYou chose "{your_paddle}" and the winner was "{winng_paddle}"'
        self.write(text,move=False,font=FONT_STYLE,align=ALIGN)
    