import turtle
import os

try:
    import winsound
except ImportError:
    pass

import highscores
import game
# The game file is imported as we actually start an instance of it 
# here.

class Menu:
    def __init__(self, play: bool = False):
        self.play = play

    def setup(self):
        turtle.clear()
        turtle.hideturtle()
        turtle.bgpic("resources/menu_background.png") # This is sized to fit to the 500x500 pixel screen
        turtle.title("Avoid! Menu")
        turtle.setup(width=500, height=500)

    def start(self):
        self.setup()
        if self.play:
            try:
                winsound.PlaySound("resources/start.wav", winsound.SND_FILENAME)
            except NameError:
                pass
        turtle.onscreenclick(self.click, btn=1)
        turtle.listen(1.0, 1.0)
        turtle.mainloop()

    def click(self, x: float, y: float):
        if y > -130.0 and y < 26.0: # This is the y value of the bar where the level options are.
            if x > -165.0 and x < -70.0: # The x of button "1"
                self.launch_game("level-one")
            elif x > -70.0 and x < 40.0: # The x of button "2"
                self.launch_game("level-two")
            elif x > 40.0 and x < 150.0: # The x of button 3
                self.launch_game("level-three")
        elif y > -207.0 and y < -170.0:
            if x > -38.0 and x < 13.0:
                self.launch_highscores()

    def launch_highscores(self):
        new_highscores = highscores.Highscores()
        new_highscores.start()
    
    def launch_game(self, level: str):
        turtle.bgpic("resources/game_background.png")
        current_game = game.Game((0, -160)) # Actually launching a new game
        game.setup()
        current_game.start(level)