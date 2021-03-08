# Avoid

Avoid is a game that I wrote in Python using the turtle library.

All the libraries used in it are default ones so there is no need to install anything...

All the sounds apart from `win.wav` were sourced from https://myinstants.com/, `win.wav` is from https://arcade.acadamy/resources.html

## Screenshots

### Menu

![Menu](https://github.com/MhmCats/Avoid/blob/main/assets/menu.png)

### Game

![Game](https://github.com/MhmCats/Avoid/blob/main/assets/game.png)


## Running

If you wish to run it then type into your terminal (with git installed):

```sh
$ git clone https://github.com/MhmCats/Avoid.git
$ cd Avoid/src
$ python3 main.py
```

There is also an optional arguement that you can pass:
```sh
$ python3 main.py --startsound
```
This will play a sound upon starting.

As well as this there is a `--level` arguement that boots the game straight into the level:
```sh
$ python3 main.py --level level-one
```

Feel free to make your own levels but due to the weird implementation that I decided to use they might not turn out as planned...

## Bugs

If you find any bugs then please make a pull request or an issue.
