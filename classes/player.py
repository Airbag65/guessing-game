class Player:
	def __init__(self, name):
		self.name = name
		self.guesses = 0

	def guess(self) -> int:
		self.guesses += 1
		return int(input("Enter your guess: "))