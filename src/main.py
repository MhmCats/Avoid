import turtle
import os
import _tkinter
import time

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
