import turtle
import os
import _tkinter

import menu
# Importing the menu as we have to start off in the menu screen

if __name__ == "__main__":

    try:
        start_menu = menu.Menu(play=True) # The Menu class' __init__ being called
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