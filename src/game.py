import turtle
import os

from level_handler import load_level
import menu

class Objects:
    def __init__(self):
        pass

    @staticmethod
    def draw_box():
        turtle.color("white")

        turtle.penup()
        turtle.goto(-200,200)
        turtle.pendown()
        turtle.goto(200,200)
        turtle.goto(200,-200)
        turtle.goto(-200,-200)
        turtle.goto(-200,200)
        turtle.penup()

    @staticmethod
    def draw_level(level_id):
        turtle.speed(0)
        level = load_level(level_id)

        for j in range(0, 20):
            y = (j-j*2)*20+200
            for i in range(0, 20):
                if level[j][i] == "x":
                    turtle.color("red")
                    turtle.pendown()
                elif level[j][i] == "w":
                    turtle.color("green")
                    turtle.pendown()
                else:
                    turtle.penup()
                x = ((i*20)-200)
                turtle.goto(x, y)
                turtle.penup()
            turtle.goto(-200, y-20)

class Game:
    def __init__(self, pos):
        self.pos = pos
        self.playing = True
        self.level = None
        self.player = turtle.Turtle()
    
        self.player.shape("square")
        self.player.color("white")
        self.player.pensize(20)
        self.player.penup()
        self.player.hideturtle()

        self.score = 0

    def start(self, level):
        turtle.clear()
            
        Objects.draw_level(level)
        Objects.draw_box()
        self.level = level
        self.player.showturtle()
        
        self.listeners()
        
        while self.playing is True:
            self.update()
        
        if self.playing == "win":
            print("You won and scored " + str(self.score))
            self.player.hideturtle()
            next_menu = menu.Menu()
            next_menu.start()
        elif not self.playing:
            print("You died!")
            self.player.hideturtle()
            next_menu = menu.Menu()
            next_menu.start()
            

    def listeners(self):
        turtle.onkey(self.forward, "w")
        turtle.onkey(self.backwards, "s")
        turtle.onkey(self.left, "a")
        turtle.onkey(self.right, "d")
        turtle.listen()

    def update(self):
        self.player.goto(self.pos)
    
    def current_level(self):
        return load_level(self.level)

    def forward(self):
        self.score += 1
        level = self.current_level()
        if self.pos[1] != 180:
            self.pos = (self.pos[0], self.pos[1]+20)
            if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)] == "x":
                self.playing = False
            elif level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)+1] == "x":
                self.playing = False
            if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)] == "w":
                self.playing = "win"
            elif level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)+1] == "w":
                self.playing = "win"

        else:
            self.playing = False
        

    def backwards(self):
        self.score += 1
        level = self.current_level()
        if self.pos[1] != -180:
            self.pos = ((self.pos[0], self.pos[1]-20))
            if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)] == "x":
                self.playing = False
            elif level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)+1] == "x":
                self.playing = False
            if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)] == "w":
                self.playing = "win"
            elif level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)+1] == "w":
                self.playing = "win"

        else:            
            self.playing = False
        

    def left(self):
        self.score += 1
        level = self.current_level()
        if self.pos[0] != -180:
            self.pos = ((self.pos[0]-20, self.pos[1]))
            if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)] == "x":
                self.playing = False
            elif level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)+1] == "x":
                self.playing = False
            if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)] == "w":
                self.playing = "win"
            elif level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)+1] == "w":
                self.playing = "win"
        else:
            self.playing = False

    def right(self):
        self.score += 1
        level = self.current_level()
        if self.pos[0] != 180:
            self.pos = ((self.pos[0]+20, self.pos[1]))
            if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)] == "x":
                self.playing = False
            elif level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)+1] == "x":
                self.playing = False
            if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)] == "w":
                self.playing = "win"
            elif level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)+1] == "w":
                self.playing = "win"
        else:
            self.playing = False

def setup():
    turtle.speed(0)
    turtle.bgcolor("black")
    turtle.shape("square")
    turtle.title("Avoid!")
    turtle.pensize(20)
    turtle.setup(width=500, height=500)
    turtle.hideturtle()