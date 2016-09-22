__author__ = 'Thomas Hauth, Martin Heck'

import unittest
import logging
import HangManEngine

# python -m unittest discover
# file names must start with "test*.py"
class HangManEngineTest(unittest.TestCase):
	def test_getStartString(self):
		hangManEngine = HangManEngine.HangManEngine('NOTTESTING')
		self.assertEqual(hangManEngine.getMessage(),
		'This is a game of hangman. For an explanation, please search the web.' )
	
	def test_readAndReturnCharacter(self):
		hangManEngine = HangManEngine.HangManEngine('NOTTESTING')
		self.assertEqual(hangManEngine.readInput('A'),
		'A')
	
	def test_printInput(self):
		hangManEngine = HangManEngine.HangManEngine('NOTTESTING')
		self.assertEqual(hangManEngine.printInput('A'),
		'You chose "A".')
	
	def test_isInWord(self):
		hme = HangManEngine.HangManEngine('NOTTESTING')
		self.assertTrue(hme.isInWord('N'))
	
	def test_isNotInWord(self):
		hme = HangManEngine.HangManEngine('NOTTESTING')
		self.assertFalse(hme.isInWord('A'))
		
	def test_guessTrue(self):
		hme = HangManEngine.HangManEngine('NOTTESTING')
		self.assertEqual(hme.guessTrue('N'),\
		'Guess correct!')
