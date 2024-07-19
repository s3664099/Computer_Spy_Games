#!/usr/bin/env python3

import loader
import sys
import util
from random import randint

"""
Title: Spy-Q Test
Author: Jenny Tyler & Chris Oxlade
Translator: David Sarkies
Version: 0.1
Date: 17 July 2024
Source: https://archive.org/details/Computer_Spy_Games
This game can be found on page 8 of Computer Spy Games, and it a python3 translation.
"""

instructions = "As a new recruit at Spy School, you've a lot of Spy Q tests to pass if you are\n"
instructions = "{}to move up through the Grades. You start as lowest of the low - a Grade 5\n".format(instructions)
instructions = "{}Trainee Spy. Your goal is to reach the top and become a Grade 1 VIS* and\n".format(instructions)
instructions = "{}even achieve the ultimate accolade: the Super Spy Award.\n".format(instructions)
instructions = "{}In each Spy Q Test, you are given ten positions on your computer screen.\n".format(instructions)
instructions = "{}You are then given numbers between 1 and 100. Your aim is to put these\n".format(instructions)
instructions = "{}numbers in order into the ten positions, with the lowest in position 1\n".format(instructions)
instructions = "{} and the highest in 10.\n".format(instructions)
instructions = "{}You are allowed to discard some numbers if they won't fit by pressing D.\n".format(instructions)
instructions = "{}The number of numbers you are allowed to discard is the same as the number\n".format(instructions)
instructions = "{}of your grade.\n\n*Very Important Spy\n".format(instructions)

grades = ["VIS","SPY","JUNIOR SPY","SPYING ASSISTANT","TRAINEE SPY"]

def main_game():
	
	positions = [0,0,0,0,0,0,0,0,0,0]
	level = 5
	game_ended  = False

	while (not game_ended):
		game_ended = turn(positions,level)

def display_grade(grade,comment,positions):

	util.clear_screen()
	print("You are {} a {}".format(comment,grade))

	position_display = ""

	for x in range (10):
		position_display = "{}{}: ".format(position_display,x)

		if (positions[x]>0):
			position_display = "{}{} ".format(position_display,positions[x])

	print(position_display)

def get_input(tries,number,positions):

	position = 100
	correct_input = False

	while (not correct_input):
		instructions = input("Where will you put {}: ".format(number))

		if (instructions == "d"):
			if tries == level:
				print("You have run out of swaps")
			else:
				tries+=1
				correct_input == True
		else:
			try:
				instructions = int(instructions)

				if ((instructions<0) or (instructions>9)):
					print("You have to enter an integer between 0 and 9")
				else:
					if (positions[instructions] != 0):
						print("That position has already been taken")
					else:
						correct_input = True
						position = instructions
			except:
				print("You have to enter an integer between 0 and 9")

	return position

def turn(positions,level):

	tries = 0
	no_positions = 10
	grade_comment = ""

	while(True):
		util.clear_screen()
		display_grade(grades[level-1],grade_comment,positions)

		number = randint(1,99)
		correct_input = False

		position = get_input(tries,number,positions)

		if (position != 100):
			positions[position] = number

	#Gets Positions
	#Places the number in position
	#Validates the position
	#Checks if ended
	#If end, checks if in order
	#If so, advances to next grade
	#Other wise fails.	

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Spy-Q Test",sys.modules[__name__])

"""

80 LET I=1


190 LET F=0
200 FOR L=P TO 10
210 IF N(L)<M AND N(L)<>0 THEN LET F=1
220 NEXT L
230 FOR L=1 TO P
240 IF N(L)>M AND N(L)<>0 THEN LET F=1
250 NEXT L
260 IF F=1 THEN GOTO 360
270 LET I=I+1:IF I<11 THEN GOTO 90
280 LET D=D-1:IF D=0 THEN GOTO 330
290 PRINT "WELL DONE, GO TO GRADE ";D
300 PRINT:PRINT "YOU ARE NOW A ";N$(D)
310 LET W$=""
320 GOTO 400
330 PRINT "TERRIFIC - YOU HAVE REACHED"
340 PRINT "THE GRADE OF SUPER SPY"
350 STOP
360 PRINT "WRONG! NOT GOOD ENOUGH"
370 PRINT N$(D)
390 LET W$="STILL"
400 PRINT:PRINT "DO YOU WANT TO TRY AGAIN? (Y/N)"
410 INPUT A$:IF A$="Y" THEN GOTO 60
420 STOP
"""