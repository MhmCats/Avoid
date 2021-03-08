import turtle
import os
import time

try:
    import winsound
except ImportError:
    pass

from data_handler import load_level, update_highscores, get_highscores
import menu
import end_screen

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
        # Here you can see the dodgy maths implementation of "json file to level"
        # it runs through the json file and if it finds a "x" then puts the pen down.
        # Naturally it runs through the screen at the same time and goes in the same
        # direction as the json file.
        for j in range(0, 20):
            y = (j-j*2)*20+200
            for i in range(0, 20):
                if level[j][i] == "x": # Blocks that kill you.
                    turtle.color("red")
                    turtle.pendown()
                elif level[j][i] == "w": # The one that, if you hit, you win.
                    turtle.color("green")
                    turtle.pendown()
                else:
                    turtle.penup()
                x = ((i*20)-200)
                turtle.goto(x, y)
                turtle.penup()
            turtle.goto(-200, y-20)

class Game:
    def __init__(self, pos: tuple):
        self.pos = pos
        self.playing = True
        self.level = None
        self.back = False
        self.player = turtle.Turtle()
        
        self.player.shape("square")
        self.player.color("white")
        self.player.pensize(20)
        self.player.penup()
        self.player.hideturtle()

    def start(self, level: str):
        turtle.clear() # If, for some reason, there is something drawn on the screen
            
        Objects.draw_level(level) # Drawing the level in!!
        Objects.draw_box() # Drawing the white box around it.
        self.level = level
        self.player.showturtle()
        
        self.listeners()
        start_time = time.time() # This is for the score.
        
        while self.playing is True: # The main game loop.
            if self.back is True: # If the user wishes to go back to the main menu.
                self.playing = "back"
            self.update() # Calling the function that actually moves the player.
        
        if self.playing == "win": # Winning
            score = int((time.time() - start_time)) * 2
            # The score is calculates by, as you can see, taking the time in seconds 
            # and multiplying it by 2. The aim is to get a low score.
            
            self.update_scores(self.level, score)

            self.player.hideturtle()
            try:
                winsound.PlaySound("resources/win.wav", winsound.SND_FILENAME)
            except NameError:
                pass
            new_end_screen = end_screen.EndScreen()
            new_end_screen.start("win", score)

        elif self.playing == "back":
            self.player.hideturtle()
            next_menu = menu.Menu()
            next_menu.start()

        elif not self.playing:
            self.player.hideturtle()
            try:
                winsound.PlaySound("resources/game_over.wav", winsound.SND_FILENAME)
            except NameError:
                pass
            new_end_screen = end_screen.EndScreen()
            new_end_screen.start("lose")

    def update_scores(self, level_id: str, new_score: int):
        if get_highscores(level_id) == 0:
            update_highscores(level_id, new_score)
        
        elif get_highscores(level_id) <= new_score:
            pass
        
        elif get_highscores(level_id) > new_score:
            update_highscores(level_id, new_score)
            

    def listeners(self):
        # Checking for key presses.
        # I might also add the arrow keys instead of WASD
        turtle.onkey(self.forward, "w")
        turtle.onkey(self.backwards, "s")
        turtle.onkey(self.left, "a")
        turtle.onkey(self.right, "d")
        turtle.onscreenclick(self.back_event)
        turtle.listen(1.0, 1.0)

    def back_event(self, x: float, y: float):
        # If the user wants to go back to the menu, first we must check the coordinates
        # of their click.
        if y > 207 and y < 250:
            if x > -250 and x < -223:
                self.back = True

    def current_level(self) :
        # The current level that we are playing
        return load_level(self.level)

    def update(self):
        # This is called in a while loop if the game is playing.
        # The movement functions do not actually move the player but they change a attribute called pos
        # then this function moves the player to the pos.
        self.player.goto(self.pos)

    def forward(self):
        level = self.current_level()
        if self.pos[1] != 180:
            self.pos = (self.pos[0], self.pos[1]+20)
            if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)] == "x":
                # This maths is basically converting the coordinates to the position of the space that 
                # we just moved to in the json file.
                self.playing = False # Dies
            try:
                if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)+1] == "x":
                    self.playing = False
            except IndexError:
                pass
            if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)] == "w":
                self.playing = "win" # Victory
            try:
                if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)+1] == "w":
                    self.playing = "win"
            except IndexError:
                pass

        else:
            self.playing = False

        # All the other movement functions are basically the same as this just updating
        # different values on the pos.
        

    def backwards(self):
        level = self.current_level()
        if self.pos[1] != -180:
            self.pos = ((self.pos[0], self.pos[1]-20))
            if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)] == "x":
                self.playing = False
            try:
                if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)+1] == "x":
                    self.playing = False
            except IndexError:
                pass
            if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)] == "w":
                self.playing = "win"
            try:
                if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)+1] == "w":
                    self.playing = "win"
            except IndexError:
                pass

        else:            
            self.playing = False
        

    def left(self):
        level = self.current_level()
        if self.pos[0] != -180:
            self.pos = ((self.pos[0]-20, self.pos[1]))
            if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)] == "x":
                self.playing = False
            try:
                if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)+1] == "x":
                    self.playing = False
            except IndexError:
                pass
            if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)] == "w":
                self.playing = "win"
            try:
                if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)+1] == "w":
                    self.playing = "win"
            except IndexError:
                pass
        else:
            self.playing = False

    def right(self):
        level = self.current_level()
        if self.pos[0] != 180:
            self.pos = ((self.pos[0]+20, self.pos[1]))
            if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)] == "x":
                self.playing = False
            try:
                if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)+1] == "x":
                    self.playing = False
            except IndexError:
                pass
            if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)] == "w":
                self.playing = "win"
            try:
                if level[int((self.pos[1]-200)/20-(self.pos[1]-200)/20*2)][int((self.pos[0]+200)/20)+1] == "w":
                    self.playing = "win"
            except IndexError:
                pass
        else:
            self.playing = False

def setup(): # This sets up the game screen (not sure why it isn't in the class...)
    turtle.speed(0)
    turtle.shape("square")
    turtle.title("Avoid!")
    turtle.pensize(20)
    turtle.setup(width=500, height=500)
    turtle.hideturtle()