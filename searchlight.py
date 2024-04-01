#!/usr/bin/env python3

import loader
import sys
import util
from random import randint

"""
Title: Searchlight
Author: Jenny Tyler & Chris Oxlade
Translator: David Sarkies
Version: 0.1
Date: 29 Marc 2024
Source: https://archive.org/details/Computer_Spy_Games
This game can be found on page 4 of Computer Spy Games, and it a python3 translation.

- Add Alarm when player spotted
- Graphics - bush, tree, building, boulder (Randomised)
"""

instructions = "A mission most secret and desperately dangerous must be undertaken this\n"
instructions = "{}very night - by you.\n".format(instructions)
instructions = "{}You must cross a closely watched section of enemy territory and return,\n".format(instructions)
instructions = "{}avoiding their gigantic and very powerful searchlight. There are rocks,\n".format(instructions)
instructions = "{}bushes and other obstacles to hide behind, but there are no second chances -\n".format(instructions)
instructions = "{}once they've seen you, you've had it. When you have completed one mission\n".format(instructions)
instructions = "{}successfully, there is another, even more difficult, to undertake. Keep\n".format(instructions)
instructions = "{}going, we are all depending on your success.\n".format(instructions)
instructions = "{}Use key M to move right and N to move left. To complete one mission you\n".format(instructions)
instructions = "{}must go right across from left to right and back again.".format(instructions)

game_level = 1
map_pos = 12
player_ypos = 13
screen_size = 15
screen_width = 20

#Create game map
gameMap = ["== = = ==  == = = ==",
			"==  = ==  == =  == =",
			"==  = ==  == =  == =",
			"=  ==  = =  =   =  =",
			"=  =  =   =   ==   =",
			"=   =   = =   =    =",
			"=    =  =    =   = =",
			"=   =    =    =    ="]

def main_game():

	score = 0
	have_file = 0
	player_xpos = 0	
	timer=0
	map_level  = gameMap[game_level]
	light_on = False
	light_counter = 0
	light_timer = 0

	#Main Game loop
	while (have_file < 3):
		util.clear_screen()
		display_screen(map_level,player_xpos,light_on)
		action = util.input_with_timeout_no_comment("",1)
		player_xpos,have_file,score = process_action(action,player_xpos,have_file,score)

		#Checks if player has been spotted
		timer += 1
		light_on,light_counter,light_timer = search_light(light_on,light_counter,light_timer,game_level)

		if (light_on):
			have_file = check_light(map_level[player_xpos],have_file)

		#Checks to see if player moves up a level
		if (have_file == 2):
			have_file,map_level = next_level()

	#End game
	print("You have been seen!")
	print("You score: ".format(game_level+(score/timer)))

	return True


#Moves the player to the next level
def next_level():

	global game_level
	game_level += 1

	if (game_level == 8):
		game_level = 7

	map_level = gameMap[game_level]
	have_file = 0

	return have_file,map_level

#Function to check if the player has been spotted
def check_light(cover,have_file):

	if (cover == " "):
		have_file = 3

	return have_file

#Function for determining when the light turns on and off
def search_light(light_on,light_counter,light_timer,level):

	if (light_counter == light_timer):
		light_on = not light_on
		light_counter = 0

		if (light_on == True):
			light_timer = randint(0,4+(6-level))
		else:
			light_timer = randint(0,5+(4-level))
	else:
		light_counter += 1

	return light_on,light_counter,light_timer

def process_action(action,player_xpos,have_file,score):

	new_pos = player_xpos

	#moves player, and sets the boundaries that the player cannot move beyond
	if (action.lower() == "m"):
		new_pos += 1
		if (new_pos >= screen_width):
			new_pos = player_xpos

	elif (action.lower() == "n"):
		new_pos -=1
		if (new_pos<0):
			new_pos = player_xpos

	#Checks if the player has made it to the edge of the screen
	if ((new_pos == screen_width-1) and (have_file == 0)):
		have_file = 1
	elif ((new_pos == 0) and (have_file == 1)):
		have_file = 2

	#If the player moves, then the score is increased
	if (player_xpos != new_pos):
		score +=1

	player_xpos = new_pos

	return player_xpos,have_file,score

def display_screen(map_level,player_xpos,light_on):

	display = ""

	for i in range(screen_size):

		if (i == map_pos):
			display = "{}{}\n".format(display,map_level)
		elif (i == player_ypos):
			for j in range(screen_width):
				if (j==player_xpos):
					display = "{}{}".format(display,'X')
				else:
					display = "{} ".format(display)
			display = "{}\n".format(display)
		elif ((i == 3) and (light_on == True)):
			display = "{}          *           \n".format(display)
		else:
			display = "{}\n".format(display)

	print(display)

"""

240 LET X=4:LET Y=1:LET B$="YOU HAVE BEEN SEEN"
250 GOSUB 380:PRINT
260 PRINT "YOU SCORE ";INT((A-1+S/G)*100)
270 PRINT:PRINT "ANOTHER GO? (Y/N)"
280 INPUT C$:IF C$="Y" THEN RUN
290 PRINT "BYE.....":STOP

"""


#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Searchlight",sys.modules[__name__])