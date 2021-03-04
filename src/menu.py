import turtle
import os
import game

class Menu:
    def __init__(self):
        pass

    def setup(self):
        turtle.hideturtle()
        turtle.clear()
        turtle.speed(0)
        turtle.bgpic("resources/menu_background.png")
        turtle.title("Avoid! Menu")
        turtle.pensize(20)
        turtle.color("white")
        turtle.setup(width=500, height=500)

    def start(self):
        self.setup()
        turtle.onscreenclick(self.click, btn=1)
        turtle.listen(1.0, 1.0)
        turtle.mainloop()

    def click(self, x, y):
        if y > -130.0 and y < 26.0:
            if x > -165.0 and x < -70.0:
                self.launch_game("level-one")
            elif x > -70.0 and x < 40.0:
                self.launch_game("level-two")
            elif x > 40.0 and x < 150.0:
                self.launch_game("level-three")
        else:
            pass
    
    def launch_game(self, level):
        turtle.bgpic("resources/game_background.png")
        current_game = game.Game((0, -160))
        game.setup()
        current_game.start(level)