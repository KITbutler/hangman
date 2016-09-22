__author__ = 'Thomas Hauth, Martin Heck'

class HangManEngine:
	def __init__(self, secretWord):
		self.secretword = secretWord
		self.guesses = []
		pass
	
	def getMessage(self):
		return\
		'This is a game of hangman. For an explanation, please search the web.'
	
	def readInput(self, letter):
		return\
		letter
	
	def printInput(self, letter):
		return\
		'You chose \"'+letter+'\".'
	
	def isInWord(self, letter):
		if letter in self.secretword:
			return True
		else:
			return False
	
	def guessTrue(self, letter):
		return 'Guess correct!'