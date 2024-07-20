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
	
	level = 5
	game_continuing = True
	grade_comment = ""

	while (game_continuing):
		course_result = turn(level,grade_comment)

		if (not course_result):
			level -= 1

			if (level>0):
				print("Well done, go to grade {}.".format(level))
				print("You are now a {}.".format(grades[level-1]))
				input("Press enter")
			else:
				print("Congratulations, you are now a Super Spy!")
				game_continuing = False

		else:
			grade_comment = "still"
			game_continuing = util.play_again(game_continuing)

def display_grade(grade,comment,positions):

	util.clear_screen()
	print("You are {} a {}".format(comment,grade))

	position_display = ""

	for x in range (10):
		position_display = "{}\n({}: ".format(position_display,x)

		if (positions[x]>0):
			position_display = "{}{} ".format(position_display,positions[x])

	print(position_display)

def get_input(tries,number,positions,level):

	position = 100
	correct_input = False

	while (not correct_input):
		instructions = input("Where will you put {}: ".format(number))

		if (instructions.upper() == "D"):
			if tries == level:
				print("You have run out of swaps")
			else:
				#tries+=1
				correct_input = True
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

	return position,tries

def turn(level,grade_comment):

	tries = 0
	no_positions = 10
	positions = [0,0,0,0,0,0,0,0,0,0]
	failed_course = False
	continuing_course = True

	while(continuing_course):
		#util.clear_screen()
		display_grade(grades[level-1],grade_comment,positions)

		number = randint(1,99)
		position,tries = get_input(tries,number,positions,level)

		if (position != 100):
			positions[position] = number
			valid_move = validate_position(positions,position)

			if (valid_move):

				if (not check_moves(positions)):
					failed_course = False
					continuing_course = False

			else:
				print("Wrong, not good enough {}.".format(grades[level-1]))
				failed_course = True
				continuing_course = False

	return failed_course

def check_moves(positions):

	moves_left = 0
	continuing = True

	for x in positions:
		if x != 0:
			moves_left += 1

	if (moves_left == 10):
		continuing = False

	return continuing

def validate_position(positions,position):

	valid_position = True

	for x in range(position,10):
		if ((positions[x]<positions[position]) and (positions[x] != 0)):
			valid_position = False

	for x in range(0,position):
		if ((positions[x]>positions[position]) and (positions[x] != 0)):
			valid_position = False

	return valid_position

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Spy-Q Test",sys.modules[__name__])