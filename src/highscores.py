import turtle
import menu

class Highscores:
	def __init__(self):
		pass

	def setup(self):
		turtle.hideturtle()
		turtle.bgpic("resources/highscore_background.png")
		turtle.setup(width=500, height=500)
		turtle.title("Avoid! Highscores")

	def start(self):
		self.setup()
		turtle.onscreenclick(self.click, btn=1)
		turtle.listen(1.0, 1.0)
		turtle.mainloop()

	def click(self, x: float, y: float):
		if y > 207 and y < 250:
			if x > -250 and x < -223:
				new_menu = menu.Menu()
				new_menu.start()