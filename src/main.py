import turtle
import os
import _tkinter

import menu
# Importing the menu as we have to start off in the menu screen

if __name__ == "__main__":
    print("Avoid!\n\nA game where you must avoid all obsticales in your path and be as fast as possible."
          "\n\nControls\n\nThe controls are WASD\n\nMisc\n\nThe arrow in the corner of the screen in the game"
          "is a back button that takes you to the menu.\n\nFind the source code at https://github.com/MhmCats/Avoid.\n\n")
    
    if not os.path.exists("resources/highscores.json"):
        with open("resources/highscores.json", "w") as f:
            json_file_content = """\
{
    "level-one": 0,
    "level-two": 0,
    "level-three": 0
}"""
            f.write(json_file_content)

    try:
        start_menu = menu.Menu() # The Menu class' __init__ being called
        start_menu.start()       # and then the start method.
    except KeyboardInterrupt:    # This was just for a smooth exit.
        print("\nExiting...")
        os._exit(1)
    except _tkinter.TclError:
    	print("\nExiting...")
    	os._exit(1)
    except turtle.Terminator:
    	print("\nExiting...")
    	os._exit(1)