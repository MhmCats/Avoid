import turtle
import os
import _tkinter

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--startsound",
                    help="Play the start sound or not.", 
                    action="store_true")

args = parser.parse_args()

import menu
# Importing the menu as we have to start off in the menu screen

if __name__ == "__main__":

    try:
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