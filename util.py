from os import system
from inputimeout import inputimeout, TimeoutOccurred
from pynput import keyboard
import time
import select
import sys

"""
Title: Util.py
Author: David Sarkies
Version: 1.1
Date: 26/1/2021

This file holds functions that are likely to be used across multiple
programs. The clear screen fuction operates under unix-like operating systems.

TimeoutExpired, alarm_handler, and input_with_timeout are fuctions that are
designed to limit the amount of time the user has to input a response. Unfortunately
the user will need to press enter to record the response.

The following package is required:
https://pypi.org/project/inputimeout/

Update 7/2/2021
Added a second input function that doesn't display 'too late'

Update 22/10/2022
Added a few more since, including a start game function that pretty much does what
all the games do at the beginning.
Added another input with timeout function to return true or false

Update 19/11/2022
Added an inkey function
"""

#Performs the start game functions.
def start_game(title):

	#Sets the replay flag
	replay = True
	answer = False
	clear_screen()
	print(title)

	answer = ask_instructions()

	return answer,replay

def clear_screen():
	_ = system('clear')

#Exception that is called when the time limit expires
class TimeoutExpired(Exception):
	print("Time Out")

def alarm_handler(signum, frame):
	raise TimeoutExpired

#Timeout function. Takes a prompt and a time in seconds
#For the timeout
def input_with_timeout(prompt, timeout):
	
	keypress = ""

	#Waits for the user input
	try:
		keypress = inputimeout(prompt, timeout)

	#If the time limit expires an error is thrown.
	except TimeoutOccurred:
		print("Too late!")
	return keypress

def input_with_timeout_02(prompt,timeout):

	try:
		inputimeout(prompt,timeout)

	except:
		return False
	return True

def input_with_timeout_no_comment(prompt, timeout):

	keypress = ""

	#Waits for the user input
	try:
		keypress = inputimeout(prompt, timeout)

	#If the time limit expires an error is thrown.
	except TimeoutOccurred:
		pass
	return keypress

#Handles asking the player a yes or no question
def yes_or_no(answer):

	reply=""

	correct = False

	#Loop while waiting for the correct answer
	while not correct:

		print()	
		reply = input()

		#When using the inkey function, this is the way to flush the
		#inputs that have been stored
		reply = reply[len(reply)-1]

		#Sets the flag as correct, and the player will replay
		if reply.upper() == "Y":
			answer = True
			correct = True

		#Sets the flag as correct and the player won't replay
		elif reply.upper() == "N":
			answer = False
			correct = True

		#Response for incorrect answer
		else:
			print()
			print("Please enter Y or N")
			print()
	return answer

#Function to handle query whether player wishes to replay the game
def play_again(replay):

	print()
	print("Do you wish to play again (Y/N) ?")

	replay = yes_or_no(replay)
	clear_screen()

	return replay

#Asks if the player wants instructions
def ask_instructions():

	#Asks player if they would like instructions
	answer = False

	print("Would you like instructions (Y/N) ?")
		
	#Calls the yes or no function
	answer = yes_or_no(answer)

	return answer

#Function that asks the player for a number between a min and max
#Checks if the response falls within the listed parameters and returns if it does
def get_num_input(description,minimum,maximum):

	#Sets query and correct flag
	correct = False
	query = -1

	#Loop while the response is incorrect
	while not correct:

		query = input("{} ({}-{}): ".format(description,minimum,maximum))

		try:
			query = int(query)

			#Does it fall within the parameters
			correct = check_range(query,minimum,maximum)

		#Is it a number
		except:
			print("Please enter a number between {} and {}".format(minimum,maximum))

	return query

#Checks if the query falls within the parameters
def check_range(number,minimum,maximum):

	correct = False

	#Does it fall within the parameters
	if number > maximum:
		print("Please enter a number less than {}".format(maximum))
	elif number < minimum:
		print("Please enter a number greater than {}".format(minimum))
	else:
		correct = True

	return correct

#Function that asks the player for a decimal between a min and max
#Checks if the response falls within the listed parameters and returns if it does
def get_float_input(description,minimum,maximum):

	#Sets query and correct flag
	correct = False
	query = -1

	#Loop while the response is incorrect
	while not correct:

		query = input("{} ({}-{}): ".format(description,minimum,maximum))

		try:
			query = float(query)
			correct = check_range(query,minimum,maximum)

		#Is it a float
		except Exception as e:

			print("Please enter a number between {} and {}".format(minimum,maximum))

	return query

#Returns a positive number
def get_number_input(description):

	#Sets the query and correct flag
	correct = False
	query = -1

	#Loop while response is incorrect
	while not correct:
		query = input("{}: ".format(description))

		try:
			query = float(query)

			if (query <1):
				print("Please enter a positive number")
			else:
				correct = True
		except:
			print("Please enter a positive number")

	return query

#Function to replicate the inkey/get function from C64 basic
#Not working perfectly as stores the previous key presses
def inkey(time_delay):

	response = ""

	#https://pypi.org/project/pynput/
	with keyboard.Events() as events:

		#Sets a time delay for the input
		event = events.get(time_delay)

		if event is None:
			print()
		else:

			#Retrieves the keypress
			response = str(event.key)[1].upper()

	return response

def tab(times,no_spaces):

	spaces = ""
	space = ""

	for x in range(no_spaces):
		spaces = "{} ".format(spaces)

	for x in range(times):
		space = "{}{}".format(space,spaces)

	return space
