import turtle
import os
import _tkinter

import menu

def main():
    start_menu = menu.Menu()
    start_menu.start()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        os._exit(1)
    except _tkinter.TclError:
    	print("\nExiting...")
    	os._exit(1)
    except turtle.Terminator:
    	print("\nExiting...")
    	os._exit(1)