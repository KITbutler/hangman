#! /usr/bin/env python3.4

# You can use this file to start a working examples of the game Hangman, without changing it.
# You may nevertheless change it, if you like.

import HangManEngine

def main():
  # my code here
  hangManEngine = HangManEngine.HangManEngine('RAD')
  while not hangManEngine.isFinished():
      print (hangManEngine.getMessage())
      print (hangManEngine.readInput())

if __name__ == "__main__":
  main()
