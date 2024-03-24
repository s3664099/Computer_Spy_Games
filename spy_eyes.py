#!/usr/bin/env python3

import loader
import sys
import util
from random import randint

"""
Title: Spy Eyes
Author: Jenny Tyler & Chris Oxlade
Translator: David Sarkies
Version: 0.1
Date: 21 March 2024
Source: https://archive.org/details/Computer_Spy_Games
This game can be found on page 4 of Computer Spy Games, and it a python3 translation.

"""

#Makes High Score persistant
#Consider creating it so numbers won't clash

instructions = "If you think you're a good spy, try this.\n"
instructions = "{}  The computer will print the numbers 1 to 9 on your screen. Watch them like\n".format(instructions)
instructions = "{}a hawk while you press a key (any one will do). One of them moves, but which?\n".format(instructions)
instructions = "{}When you think you know, press a key again and tell the computer.\n".format(instructions)
instructions = "{}  Bet your powers of observation aren't as good as you thought.\n".format(instructions)

number_size = 9
screen_size = 9
timeout_length = 5
high_score = 0

def main_game():

	#Loads the high score (if there is one)
	try:
		f = open("se_high_score.txt", "r")
		print(f.read())		
		high_score = f.read()
		f.close()

		#Makes sure that the high score is a number
		try:
			int(high_score)
		except:
			high_score = 0

	except:
		high_score = 0

	score = 0
	replay = True

	while(replay == True):
		numbers = []
		used_coords = []
		
		for x in range(number_size):
			numbers.append(generate_tuple(x+1,used_coords))

		display_screen(numbers)
		input()
		moved_number = shift_number(numbers)
		display_screen(numbers)
		input()

		score += query_move(numbers[moved_number][1])
		print("Your score is now {}".format(score))

		#Checks if the player has a high score, and saves it.
		if (score > int(high_score)):
			high_score = score
			print("Your score is currently the high score")
			f = open("se_high_score.txt", "w")
			f.write(str(high_score))
			f.close()
		else:
			print("The high score is {}".format(high_score))

		replay = util.play_again(replay)

	return replay

def query_move(number):

	util.clear_screen()
	result = 0
	guess = input("What number moved: ")

	if (guess == str(number)):
		print("Well spied, you are correct")
		result = 1
	else:
		print("Unfortunately the correct number was {}".format(number))

	return result
	
#Generates the tuple for the numbers
def generate_tuple(num,used_coords):

	available_coord = False

	while (available_coord == False):

		#Generated random coordinate
		found_coord = False
		x_coord = randint(0,screen_size)
		y_coord = randint(0,screen_size)

		#Checks if coordinate already used
		for x in used_coords:
			if x_coord == x[0] and y_coord == x[1]:
				found_coord == True

		#If not marks as used
		if found_coord == False:
			available_coord = True
			used_coords.append((x_coord,y_coord))

	return ([x_coord,y_coord],num)

#Selects a random number and moves it
def shift_number(numbers):

	moved_number = randint(0,len(numbers))
	movement = sgn(moved_number-5.1)
	numbers[moved_number][0][0] = numbers[moved_number][0][0]+movement

	return moved_number

#So, the actually program selects the number and then uses that number to move it up or down
#Might do it that way since that is the original, but we need to make sure that it doesn't
#Overright anything. This is the function that is used to determine the move
def sgn(number):

	new_number = 0

	if (number<0):
		new_number = -1
	elif (number>0):
		new_number = 1

	return new_number

def display_screen(numbers):

	util.clear_screen()
	edge = "    "
	screen = "{}".format(edge)

	#Displays top border
	for x in range(screen_size+3):
		screen = "{}=".format(screen)

	screen = "{}\n{}=".format(screen,edge)

	#Builds in main screen
	for x in range(0,screen_size+1):
		for y in range(0,screen_size+1):

			match_coord = False
			picked_num = 0

			#Checks whether the coordinate is a number or a space
			for z in numbers:
				if (z[0][0] == x and z[0][1] == y):
					match_coord = True
					picked_num = z[1]

			if(match_coord == True):
				screen = "{}{}".format(screen,picked_num)
			else:
				screen = "{} ".format(screen)

		screen = "{}=\n{}=".format(screen,edge)

	#Displays bottom border
	for x in range(screen_size+2):
		screen = "{}=".format(screen)

	print(screen)

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Spy Eyes",sys.modules[__name__])
