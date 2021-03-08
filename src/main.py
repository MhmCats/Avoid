import turtle
import os
import _tkinter

import argparse

import menu
import game

parser = argparse.ArgumentParser(prog="python3 main.py",
                                 description="Have fun playing the beautiful start sound...",
                                 epilog="Enjoy playing Avoid!")
parser.add_argument("--startsound",
                    help=": play the start sound or not", 
                    action="store_true")
parser.add_argument("--level",
                    help=": specify a level you want to play",
                    metavar="level-name")
args = parser.parse_args()

if __name__ == "__main__":

    try:
        if not args.level is None:
            levels = ["level-one", "level-two", "level-three"]
            if args.level in levels:
                turtle.bgpic("resources/game_background.png")
                start_game = game.Game((0, -160))
                game.setup()
                start_game.start(args.level)
            else:
                turtle.bgpic("resources/game_background.png")
                start_game = game.Game((0, -160))
                game.setup()
                start_game.start("level-one")

        else:
            start_menu = menu.Menu(play=args.startsound) # The Menu class' __init__ being called
            start_menu.start()                # and then the start method.
    except KeyboardInterrupt:             # This was just for a smooth exit.
        print("\nExiting...")
        os._exit(1)
    except _tkinter.TclError:
    	print("\nExiting...")
    	os._exit(1)
    except turtle.Terminator:
    	print("\nExiting...")
    	os._exit(1)