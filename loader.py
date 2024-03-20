#!/usr/bin/env python3

import util
import time
import computer_nightmare
import number_wizard
import ghost_guzzler
import spiderwoman
import gravedigger
import mad_house
import ghost_maze
import sceance

#Function that displays the games available, and allows the user to select them
def select_game():
	
	selecting = True

	#Creates a while loops to hold the menu to select the game
	while (selecting):
		util.clear_screen()
		print("1) Computer Nightmare")
		print("2) The Number Wizard")
		print("3) Ghost Guzzler")
		print("4) Spiderwoman")
		print("5) Gravedigger")
		print("6) Mad House")
		print("7) Ghost Maze")
		print("8) Seance")
		print("X) Exit")
		print()
		response = input()

		#Executes the players selection
		if response.upper() == 'X':

			#Ends the program by letting it run out
			selecting = False

		elif response == "1":
			start_game("Computer Nightmare",computer_nightmare)
		elif response == "2":
			start_game("Number Wizard",number_wizard)
		elif response == "3":
			start_game("Ghost Guzzler",ghost_guzzler)
		elif response == "4":
			start_game("Spiderwoman",spiderwoman)
		elif response == "5":
			start_game("Gravedigger",gravedigger)	
		elif response == "6":
			start_game("Mad House",mad_house)
		elif response == "7":
			start_game("Ghost Maze",ghost_maze)
		elif response == "8":
			start_game("Sceance",sceance)
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

