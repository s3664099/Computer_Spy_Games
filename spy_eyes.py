#!/usr/bin/env python3

import loader
import sys
import util
from random import randint

"""
Title: Spy Eyes
Author: Jenny Tyler & Chris Oxlade
Translator: David Sarkies
Version: 0.0
Date: 20 March 2024
Source: https://archive.org/details/Computer_Spy_Games
This game can be found on page 4 of Computer Spy Games, and it a python3 translation.

"""

instructions = "If you think you're a good spy, try this.\n"
instructions = "{}  The computer will print the numbers 1 to 9 on your screen. Watch them like\n".format(instructions)
instructions = "{}a hawk while you press a key (any one will do). One of them moves, but which?\n".format(instructions)
instructions = "{}When you think you know, press a key again and tell the computer.\n".format(instructions)
instructions = "{}  Bet your powers of observation aren't as good as you thought.\n".format(instructions)

def main_game():
	
	#Set up an array holding nine tuples which holds the x,y positions and the number
	#Randomly assigns the positions (though they cannot be the same, or within 2 points)
	#Randomly selects one and moves it
	#Asks the player which one was moved
	#If correct gets a point, if not doesn't
	#After three shots game over
	#Saves a high score
	#Makes High Score persistant

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Spy Eyes",sys.modules[__name__])