from random import random


import random

class Ai:
	def __init__(self):
		self.guesses = 0
		self.min = 1
		self.max = 50
	
	def guess(self) -> int:
		self.guesses += 1
		return random.randint(self.min, self.max)
