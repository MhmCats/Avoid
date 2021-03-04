import turtle
import os
import _tkinter

import menu

if __name__ == "__main__":
    print("Avoid!\n\nA game where you must avoid all obsticales in your path and be as fast as possible."
          "\n\nControls:\n\nThe controls are WASD\n\nMisc\n\nThe arrow in the corner of the screen in the game"
          "is a back button that takes you to the menu.\n\nFind the source code at https://github.com/MhmCats/Avoid.\n\n")
    try:
        start_menu = menu.Menu()
        start_menu.start()
    except KeyboardInterrupt:
        print("\nExiting...")
        os._exit(1)
    except _tkinter.TclError:
    	print("\nExiting...")
    	os._exit(1)
    except turtle.Terminator:
    	print("\nExiting...")
    	os._exit(1)