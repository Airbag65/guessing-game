from random import random
from .player import Player

import random

class Ai(Player):
	def __init__(self):
		self.guesses = 0
		self.min = 1
		self.max = 50
	
	def guess(self) -> int:
		self.guesses += 1
		return random.randint(self.min, self.max)
