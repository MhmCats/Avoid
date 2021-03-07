import menu
import turtle

class EndScreen:
	def __init__(self):
		pass

	def setup(self):
		turtle.clear()
		turtle.setup(height=500, width=500)
		turtle.hideturtle()
		turtle.bgpic("resources/end_screen_background.png")
		turtle.title("Avoid! Results")

	def start(self, outcome: str, score: int = None):
		self.setup()

		if outcome == "win":
			self.draw_win(score)
		elif outcome == "lose":
			self.draw_lose()

		turtle.onscreenclick(self.click, btn=1)
		turtle.listen(1.0, 1.0)

		turtle.mainloop()

	def draw_win(self, score: int):
		turtle.goto(-230, 125)
		turtle.color("green")
		turtle.write("You won!", font=("Courier New", 72, "bold"))
		
		turtle.penup()
		
		turtle.goto(-75, 60)
		turtle.color("white")
		turtle.write(f"Score: {score}", font=("Courier New", 16, "bold"))

	def draw_lose(self):
		turtle.goto(-230, 125)
		turtle.color("red")
		turtle.write("You ded!", font=("Courier New", 72, "bold"))
		
		turtle.penup()
		
		turtle.goto(-75, 75)
		turtle.color("white")
		turtle.write("Lmao you died", font=("Courier New", 16, "bold"))

	def click(self, x, y):
		if x > -94 and x < 76:
			if y > -171 and y < -46:
				new_menu = menu.Menu()
				new_menu.start()