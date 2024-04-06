#!/usr/bin/env python3

import loader
import sys
import util
from random import randint
import searchlight_pygame as graphics
import time

"""
Title: Searchlight
Author: Jenny Tyler & Chris Oxlade
Translator: David Sarkies
Version: 0.1
Date: 29 March 2024
Updated: 6 April 2024
Source: https://archive.org/details/Computer_Spy_Games
This game can be found on page 4 of Computer Spy Games, and it a python3 translation.
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
map_pos = 7
player_ypos = 8
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
	map_level = set_graphics(gameMap[game_level])
	light_on = False
	light_counter = 0
	light_timer = 0
	starttime = time.time()
	got_file = False

	graphics.set_caption("Searchlight")
	display = graphics.display_screen()

	#Main Game loop
	while (have_file < 3):
		
		#Processes action
		new_pos = graphics.get_keypress(player_xpos)
		player_xpos,have_file,score,got_file = process_action(player_xpos,new_pos,have_file,score)
		prev_file = have_file

		#Checks if player has been spotted
		if (time.time()-starttime>0.5):
			timer += 1
			light_on,light_counter,light_timer = search_light(light_on,light_counter,light_timer,game_level)
			starttime = time.time()

		# Displays the screen
		display = graphics.clear_screen(display)
		display_screen(map_level,player_xpos,light_on,display)

		if (light_on):
			have_file = check_light(map_level[player_xpos],have_file)

		if (got_file == True):
			comment = "You got the file"
			graphics.message_display(comment,display,30,"centre")
			got_file = False

		#Checks to see if player moves up a level
		if (have_file == 2):
			comment = "You successfully returned the file"
			graphics.message_display(comment,display,30,"centre")
			have_file,map_level = next_level()

	#End game
	end_response = "You have been seen! You score: {}".format(game_level+(score/timer))
	graphics.play_sound('./sounds/siren.wav')
	graphics.message_display(end_response,display,30,"centre")
	graphics.close_screen()

	return True

#Creates a random allocation for the cover types
def set_graphics(map_level):

	new_map = ""

	for x in range(len(map_level)):
		
		if (map_level[x] == "="):
			new_map = "{}{}".format(new_map,randint(0,2))
		else:
			new_map = "{}{}".format(new_map," ")

	return new_map

#Moves the player to the next level
def next_level():

	global game_level
	game_level += 1

	if (game_level == 8):
		game_level = 7

	map_level = set_graphics(gameMap[game_level])
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

#Processes the results of the action
def process_action(player_xpos,new_pos,have_file,score):

	got_file = False

	#Sets boundaries for the screen
	if new_pos > screen_width-1:
		new_pos = screen_width -1
	elif new_pos < 0:
		new_pos = 0

	#Checks if the player has made it to the edge of the screen
	if ((new_pos == screen_width-1) and (have_file == 0)):
		have_file = 1
		got_file = True
	elif ((new_pos == 0) and (have_file == 1)):
		have_file = 2

	#If the player moves, then the score is increased
	if (player_xpos != new_pos):
		score +=1

	player_xpos = new_pos

	return player_xpos,have_file,score, got_file

def display_screen(map_level,player_xpos,light_on,graphics_display):

	for i in range(screen_size):

		if (i == map_pos):
			graphics_display = graphics.display_map(map_level,graphics_display,i)
		elif (i == player_ypos):
			graphics_display = graphics.display_player(graphics_display,player_xpos,i)
		elif ((i == 3) and (light_on == True)):
			graphics_display = graphics.display_spotlight(graphics_display,i)

	graphics.update_display(graphics_display)

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Searchlight",sys.modules[__name__])