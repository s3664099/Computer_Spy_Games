#!/usr/bin/env python3

import loader
import sys
import util
from random import randint

"""
Title: 
Author: 
Translator: David Sarkies
Version: 
Date: 
Source: https://archive.org/details/Computer_Spy_Games
This game can be found on page 4 of Creepy Computer Games, and it a python3 translation.

"""

instructions = ""

def main_game():
	
	print("Main Game")

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Spy Eyes",sys.modules[__name__])