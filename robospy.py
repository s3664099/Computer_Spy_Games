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
Version: 1.0
Date: 15 May 2024
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

def main_game():

	playing = True
	high_score = 0

	while(playing):

		score = 0
		no_moves = 1
		turn = 0
		error = False

		util.clear_screen()
		print(">>> Robospy <<<")
		input("Press Enter to continue")

		playing,high_score = game_loop(score,no_moves,turn,error,high_score)


#Main Loop
def game_loop(score,no_moves,turn,error,high_score):

	answer = True

	while (not error):
		util.clear_screen()
		print("\n\n")

		#Updates the Score
		if (turn == 5):
			no_moves += 1
			turn = 0

		#Sets the time the moves are displayed
		turn_speed = 5-(no_moves*0.5)

		if (turn_speed<0.5):
			turn_speed = 0.5

		moves = display_moves(no_moves)
		turn +=1
		time.sleep(turn_speed)

		#Get the directions
		util.clear_screen()

		#Get Moves
		error = get_player_moves(no_moves,moves)

		#If the guess was correct, score increases
		if (error == False):
			score += no_moves

			#Checks if high score beaten
			if score>high_score:
				high_score = score
		else:
			print("You lost him! Some Spy!")
			print("Score = {}".format(score))
			print("High Score = {}".format(high_score))
			print("\n\nDo you want to play again: ")
			answer = util.yes_or_no(answer)

	return answer,high_score

def display_moves(no_words):

	moves = ""

	#Build and display the moves
	for i in range(no_words):
		move = randint(0,1)

		if (move == 0):
			print("Left\n")
			moves+= "l"
		else:
			print("Right\n")
			moves+= "r"	

	return moves

#Get player moves and determines whether they were correct
def get_player_moves(no_words,moves):

	global key_pressed
	error = False
	print("What were the moves?\n")

	for i in range(no_words):

		correct_move = False
		
		#Loop continues unless correct key pressed
		while not correct_move:	
			key_pressed = ""

			listen_keyboard(
				on_press=press,
				sequential=True,
			)

			#Checks if the correct button pressed
			if ((key_pressed == "l") or (key_pressed == "r")):
				correct_move = True

				#Checks if it matches the direction
				if (key_pressed != moves[i]):
					error = True

	return error

def press(key):

	global key_pressed
	key_pressed = ""
	if key == "r" or key == "l":
		key_pressed = key
		stop_listening()

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game(">>> Robospy <<<",sys.modules[__name__])