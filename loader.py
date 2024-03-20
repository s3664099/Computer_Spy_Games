#!/usr/bin/env python3

import util
import time
import spy_eyes

#Function that displays the games available, and allows the user to select them
def select_game():
	
	selecting = True

	#Creates a while loops to hold the menu to select the game
	while (selecting):
		util.clear_screen()
		print("1) Spy Eyes")
		print("2) Search Light")
		print("3) Robospy")
		print("4) Spy Q Test")
		print("5) Secret Message Maker")
		print("6) Rendezvous")
		print("7) Morse Coder")
		print("X) Exit")
		print()
		response = input()

		#Executes the players selection
		if response.upper() == 'X':

			#Ends the program by letting it run out
			selecting = False

		elif response == "1":
			start_game("Spy Eyes",spy_eyes)
		else:
			print("You have entered an incorrect option")
			time.sleep(5)

#Start game function. Takes the input to be used, and the title of the game
def start_game(title,game):

	answer,replay = util.start_game(title)

	#Displays the instructions that are stored at the beginning of the game selected
	if answer:
		util.clear_screen()
		print(game.instructions)
		input("Press Enter to Continue: ")

	#Loop for replaying the game
	while replay:
		game.main_game()
		replay = util.play_again(replay)

if __name__ == '__main__':

	select_game()

