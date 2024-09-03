#!/usr/bin/env python3

import loader
import sys
import util
import time
import os
from random import randint

"""
Title: Morse Coder
Author: Jenny Tyler & Chris Oxlande
Translator: David Sarkies
Version: 2.0
Date: 13 August 2024
Source: https://archive.org/details/Computer_Spy_Games
This game can be found on page 16 of Computer Spy Games, and it a python3 translation.
"""

instructions = "If you want to be a really successful spy, you need to know how to send, recieve\n"
instructions = "{}and, of course, intercept messages in Morse Code. This program will help you\n".format(instructions)
instructions = "{}learn. If you have never used Morse Code before, youwill need to make yourself\n".format(instructions)
instructions = "{}a chart of letters and their Morse equivalents. Use lines 400-450  of the\n".format(instructions)
instructions = "{}program to do this. They show the Morse code for each letter of the alphabet\n".format(instructions)
instructions = "{}in order.\n".format(instructions)
instructions = "{}\nWhat you have to do\n---- --- ---- -- --\n".format(instructions)
instructions = "{}In Morse Code, each letter is represented by a series of long and short sounds\n".format(instructions)
instructions = "{}or flashes. This program uses a flashing star. it will give you the code for\n".format(instructions)
instructions = "{}a letter and then ask you which it was. You will have to watch carefully\n".format(instructions)
instructions = "{}to pick out the long and short flashes and remember them.You will see the\n".format(instructions)
instructions = "{}cursor flashing too at the left of the screen. Ignore this it has nothing\n".format(instructions)
instructions = "{}to do with the code.\n".format(instructions)

morse_code = [".-","-...","-.-","-..",".","..-","--.","....","..",".---","-.-",".-..","--","-.","---",
			  ".--","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

def main_game():
	
	util.clear_screen()

	speed = 1
	print("Morse Tester\n----- ------\n\n")
	player_speed = util.get_num_input("What Level? (1=fast, 5=slow)",1,5)
	display_style = util.get_num_input("What Style (1=visual,2=sound)",1,2)
	player_speed *= speed
	score = 0
	playing = True

	while(playing):

		util.clear_screen()
		print("Score: {}\n\n".format(score))
		print("Get Ready")
		time.sleep(player_speed)

		letter,morse_letter = select_letter()

		if display_style == 1:
			display_letter(morse_letter,player_speed)
		else:
			sound_letter(morse_letter,player_speed)

		guess = input("Type in your answer: ")

		if (guess.upper() == letter):
			print("Correct")
			score += 1
		else:
			print("No, the answer is {}".format(letter))

		if (not util.play_again(True)):
			playing = False

#Plays a beep
def beep(duration=0.2):

	beep = os.system(f"play -n synth {duration} sine 1000 vol 0.5 > /dev/null 2>&1")

#displays the letter
def display_letter(morse_letter,player_speed):
	for x in morse_letter:

		if x==".":
			display_code(1,player_speed)
		elif x=="-":
			display_code(3,player_speed)

def sound_letter(morse_letter,player_speed):

	for x in morse_letter:
		if x==".":
			beep()
		elif x=="-":
			beep(0.4)
		time.sleep(player_speed)

#Selects the letter
def select_letter():

	#Selects the letter and the morse equivalent
	letter_no = randint(65,90)
	letter = chr(letter_no)
	morse_letter = morse_code[letter_no-65]

	return letter,morse_letter

#Displays the star which represents a dot/dash
def display_code(speed,player_speed):

	#sets the position
	util.clear_screen()
	code = position(" ","\n")
	code = position(code," ")
	code = "{}*".format(code)
	code = position(code,"\n")
	print(code)

	#Sets the amount of time the star will be displayed
	time.sleep(speed*player_speed)
	util.clear_screen()
	time.sleep(player_speed)

#Positions the character on the screen
def position(code,character):

	for x in range(10):
		code = "{}{}".format(code,character)

	return code

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Morse Coder",sys.modules[__name__])