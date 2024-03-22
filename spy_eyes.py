#!/usr/bin/env python3

import loader
import sys
import util
from random import randint

"""
Title: Spy Eyes
Author: Jenny Tyler & Chris Oxlade
Translator: David Sarkies
Version: 0.0
Date: 20 March 2024
Source: https://archive.org/details/Computer_Spy_Games
This game can be found on page 4 of Computer Spy Games, and it a python3 translation.

"""

instructions = "If you think you're a good spy, try this.\n"
instructions = "{}  The computer will print the numbers 1 to 9 on your screen. Watch them like\n".format(instructions)
instructions = "{}a hawk while you press a key (any one will do). One of them moves, but which?\n".format(instructions)
instructions = "{}When you think you know, press a key again and tell the computer.\n".format(instructions)
instructions = "{}  Bet your powers of observation aren't as good as you thought.\n".format(instructions)

number_size = 9
numbers = []
used_coords = []
screen_size = 9

def main_game():

	score = 0
	
	for x in range(number_size):

		numbers.append(generate_tupple(x+1))

#Selects random numbers and confirms they have not been used
def generate_tupple(num):

	available_coord = False

	while (available_coord == False):

		found_coord = False
		x_coord = randint(4,screen_size+4)
		y_coord = randint(4,screen_size+4)

		for x in used_coords:

			if x_coord == x[0] and y_coord == x[1]:
				found_coord == True



		if found_coord == False:
			available_coord = True
			used_coords.append((x_coord,y_coord))

	return ([x_coord,y_coord],num)


	#Set up an array holding nine tuples which holds the x,y positions and the number
	#Randomly assigns the positions (though they cannot be the same, or within 2 points)
	#Randomly selects one and moves it
	#Asks the player which one was moved
	#If correct gets a point, if not doesn't
	#After three shots game over
	#Saves a high score
	#Makes High Score persistant

	"""
	*10 DIM X(9): DIM Y(9)
	*20 LET P=0
	*30 FOR I=1 TO 9
	*40 GOSUB 340: LET X(I)=N+3
	*50 GOSUB 340: LET Y(I)=N+3
	60 NEXT I
	70 GOSUB 360
	80 GOSUB 310
	90 GOSUB 340
	100 LET M=N:GOSUB 340
	110 LET X(M)=X(M)+SGN(N-5.1)
	120 GOSUB 360
	130 GOSUB 310
	140 CLS:PRINT
	150 PRINT "WHICH NUMBER MOVED"
	160 INPUT A
	170 IF A<>M THEN GOTO 250
	180 CLS:PRINT
	190 PRINT "WELL SPIED!"
	200 LET P=P+!
	210 PRINT "YOU NOW HAVE ";P;" POINTS"
	220 PRINT: PRINT "PRESS A KEY"
	230 GOSUB 310
	240 GOTO 30
	250 CLS:PRINT:PRINT "WRONG - END OF GO"
	260 PRINT "CORRECT ANSWER WAS ";M
	270 PRINT "YOU SCORED ";P;" POINTS"
	280 PRINT "ANOTHER GO? (Y/N)"
	290 INPUT A$:IF A$="Y" THEN RUN
	300 STOP
	310 LET I$=INKEY$
	320 IF I$="" THEN GOTO 310
	330 RETURN
	*340 LET N=INT(RND(1)*9)+1
	350 RETURN
	360 CLS
	370 FOR I=1 TO 9
	380 PRINT TAB(X(I),Y(I));STR$(I)
	390 NEXT I
	400 RETURN
	"""

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Spy Eyes",sys.modules[__name__])