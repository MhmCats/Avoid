import turtle

import menu
import data_handler

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
		self.draw_scores()
		turtle.onscreenclick(self.click, btn=1)
		turtle.listen(1.0, 1.0)
		turtle.mainloop()

	def draw_scores(self):
		self.draw((-80, 21), self.three_digit(data_handler.get_highscores('level-one')))
		self.draw((-80, -108), self.three_digit(data_handler.get_highscores('level-two')))
		self.draw((-80, -236), self.three_digit(data_handler.get_highscores('level-three')))

	def draw(self, start_point: tuple, value: str):
		turtle.bgpic("resources/highscore_background.png")
		turtle.setup(width=500, height=500)
		turtle.color("white")
		value = list(value)
		turtle.penup()
		turtle.hideturtle()

		for item in value:
			turtle.goto(start_point)
			turtle.write(item, font=("Courier New", 72, "bold"))

			start_point = (start_point[0] + 60, start_point[1])


	def click(self, x: float, y: float):
		if y > 207 and y < 250:
			if x > -250 and x < -223:
				new_menu = menu.Menu()
				new_menu.start()

	def three_digit(self, num: int):
		string_number = str(num)
		if len(string_number) == 3:
			return string_number

		elif len(string_number) == 2:
			return "0" + string_number

		elif len(string_number) == 1:
			return "00" + string_number

		else:
			return None
