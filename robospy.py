#!/usr/bin/env python3

import loader
import sys
import util
from random import randint

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

def main_game():
	
	print("Main Game")

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Spy Eyes",sys.modules[__name__])