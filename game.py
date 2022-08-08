import random
from classes.ai import Ai
from classes.player import Player
from time import sleep
import os

class Game:
	def __init__(self):
		p_name = input("Enter your name: ")
		os.system("cls" if os.name == "nt" else "clear")
		self.player = Player(p_name)
		self.ai = Ai()
		print(f"""
		Welcome {self.player.name}!\n
This is a Guessing Game! Your goal is to guess a random number 
between 1 and 50! You are also facing an AI opponent. 
You and the AI will take turns guessing the correct number! 
The first one to get it right, wins!\n
		LET THE GAME BEGIN!\n
		""")
		self.game_over = False
		self.winner = None
	
	def generate_number(self):
		self.correct = random.randint(1,50)
	
	def start(self):
		self.play_decision()

	def play_decision(self):
		self.generate_number()
		decision = input("Would you like to start a new game? [Y/N]\n").lower()
		if decision == "y":
			self.game_over = False
			self.play()
		elif decision == "n":
			self.quit()

	def quit(self):
		os.system("cls" if os.name == "nt" else "clear")
		print(f"\n\nSorry to see you go {self.player.name}")
		
	def play(self):
		os.system("cls" if os.name == "nt" else "clear")
		print(f"\nThe game has begun!\n{self.player.name} begins!")
		
		while not self.game_over:
			p_guess = self.player.guess()
			sleep(.75)
			if p_guess == self.correct:
				print("Thats correct!")
				print(f"{self.player.name} wins!!")
				self.player.guesses = 0
				self.ai = Ai()
				self.game_over = True
				break
			elif p_guess > self.correct:
				self.ai.max = p_guess
				print("The correct number is lower")
			elif p_guess < self.correct:
				self.ai.min = p_guess
				print("The correct nubmer is higher")
			print("\nAI's turn...")
			sleep(1)
			ai_guess = self.ai.guess()
			print(f"AI guesses: {ai_guess}")
			if ai_guess == self.correct:
				print("Thats correct!")
				print(f"AI wins!!")
				self.player.guesses = 0
				self.ai = Ai()
				self.game_over = True
				break
			elif ai_guess > self.correct:
				self.ai.max = ai_guess
				print("The correct number is lower")
			elif ai_guess < self.correct:
				self.ai.min = ai_guess
				print("The correct nubmer is higher")
			print("Yor turn agian...\n")
		sleep(2)
		self.play_decision()
	
	
	
if __name__ == "__main__":
	game = Game()
	game.start()