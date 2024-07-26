#!/usr/bin/env python3

import loader
import sys
import util
from random import randint

"""
Title: Secret Message Maker
Author: Jenny Tyler & Chris Oxlade
Translator: David Sarkies
Version: 0.1
Date: 21 July 2024
Source: https://archive.org/details/Computer_Spy_Games
This game can be found on page 10 of Computer Spy Games, and it a python3 translation.

"""

instructions = "Use this program to send coded messages to your friends. They'll need a computer\n"
instructions = "{}to decode them, but not necessarily the same type as yours. (They'll need a\n".format(instructions)
instructions = "{}copy of the program too don't forget) They can decode your messages and \n".format(instructions)
instructions = "{}then send coded messages back to you.\n".format(instructions)

def main_game():
	
	running = True

	util.clear_screen()
	print("\nSecret Message Maker")
	print("====================")

	while(running):
		correct_answer = False

		while(not correct_answer):
			print("Do you want to\n")
			print("   1. Code a Message")
			print("or 2. Decode a Message")
			print("or 3. Quit\n")
			option = input("Enter a number: ")

			if (option == "3"):
				correct_answer = True
				running = False
			elif (option == "2"):
				decode()
			elif (option == "1"):
				code()
			else:
				print("Please enter 1,2 or 3")

def get_input(query):

	return input(query)

def code_forward(message,random_num):

	coded_message = ""
	for x in range(len(message)):

		ascii_code = ord(message[x])

		if (ascii_code != 32):
			ascii_code += random_num


			if (ascii_code>90):
				ascii_code -=26
			elif (ascii_code<65):
				ascii_code +=26
		coded_message = "{}{}".format(coded_message,chr(ascii_code))

	return coded_message

def code_backward(message):

	coded_message = ""

	for x in range(len(message)-1,0,-1):
		coded_message = "{}{}".format(coded_message,message[x])

	return coded_message

def code():

	message = get_input("What is your message to be coded: ")
	message = "F{}".format(message)
	random_num = randint(0,25)
	message = code_forward(message,random_num)
	message = "{}{}".format(chr(random_num+64),code_backward(message))

	if ((len(message)/2) == (int(len(message)/2))):
		message = code_message(message)

	print("The coded message is: {}".format(message))

def code_message(message):

	coded_message = ""
	message_length = len(message)

	for x in range(0,message_length-1,2):
		coded_message = "{}{}".format(coded_message,message[x+1])
		coded_message = "{}{}".format(coded_message,message[x])

	return coded_message

def decode():
	message = get_input("What is your message to be decoded: ")
	
	if ((len(message)/2) == (int(len(message)/2))):
		message = code_message(message)

	key = message[0]
	key = ord(key)-64
	key = -key

	message = code_backward(message)
	message = code_forward(message,key)
	message = message[:len(message)-1]
	print("The decoded message is: {}".format(message))

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Spy Eyes",sys.modules[__name__])