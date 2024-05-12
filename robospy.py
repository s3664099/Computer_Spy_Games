#!/usr/bin/env python3

import loader
import sys
import util
from random import randint
import time
from sshkeyboard import listen_keyboard,stop_listening

"""
Title: Robospy
Author: Adrian Hall
Translator: David Sarkies
Version: 0.0
Date: 8 May 2024
Source: https://archive.org/details/Computer_Spy_Games
This game can be found on page 6 of Computer Spy Games, and it a python3 translation.
"""

instructions = "You are in control of Robospy - a unique remote-operation tracking device which\n"
instructions = "{}secretly follows enemy agents. You recieve details of an agent's movements\n".format(instructions)
instructions = "{}through the streets - whether he turns left or right - and you must copy\n".format(instructions)
instructions = "{}these movements exactly when you send signals to Robospy, so that it can\n".format(instructions)
instructions = "{}stay in touch with the agent.\n\n".format(instructions)
instructions = "{}Unfortunately the agent knows that Robospy is following him. He makes your\n".format(instructions)
instructions = "{}job harder the longer it keeps up. He has also managed to tamper with your\n".format(instructions)
instructions = "{}signalling device, re-arranging the keys in an attempt to confuse you. This\n".format(instructions)
instructions = "{}means that you press L (for left) with your right hand and R (for right) with\n".format(instructions)
instructions = "{}your left. Can you stick with him, or will he shake you off?\n".format(instructions)

speed = 0.3
h = 0
s = 0

def main_game():

	no_words = 1
	no_words_printed = 0

	util.clear_screen()
	print(">>> Robospy <<<")
	input("Press Enter to continue")
	util.clear_screen()
	print("\n\n")

	#Updates the Score
	if (no_words_printed == 5):
		no_words += 1
		no_words_printed = 0

	movement = ""

	moves = display_moves(no_words)
	no_words_printed +=1
	time.sleep(10*speed*no_words)
	
	#Get the directions
	util.clear_screen()

	#Get Moves
	move = get_player_moves()

def display_moves(no_words):

	moves = ""

	#Build and display the moves
	for i in range(no_words):
		move = randint(0,1)

		if (move == 0):
			print("Left\n")
			moves+= "L"
		else:
			print("Right\n")
			moves+= "R"	

	return moves

#Get player moves
def get_player_moves():

	global key_pressed
	key_pressed = ""

	listen_keyboard(
		on_press=press,
		sequential=True,
	)

	return key_pressed

def press(key):

	global key_pressed
	key_pressed = ""
	if key == "r" or key == "l":
		key_pressed = key
		stop_listening()

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game(">>> Robospy <<<",sys.modules[__name__])