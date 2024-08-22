#!/usr/bin/env python3

import loader
import sys
import util
import time
from random import randint

"""
Title: Morse Coder
Author: Jenny Tyler & Chris Oxlande
Translator: David Sarkies
Version: 0.1
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
	speed = 3
	print("Morse Tester\n----- ------\n\n")
	player_speed = util.get_num_input("What Level? (1=fast, 5=slow)",1,5)
	player_speed *= speed
	util.clear_screen()
	print("Get Ready")
	time.sleep(player_speed)

"""
110 FOR T=1 TO 20*S:NEXT T
120 GOSUB 310
130 LET F$=M$(ASC(Q$)-64)
140 GOSUB 220
150 CLS:PRINT
160 PRINT "TYPE IN YOUR ANSWER"
170 INPUT X$
180 IF X$=Q$ THEN PRINT "CORRECT"
190 IF X$<>Q$ THEN PRINT "NO. THE ANSWER IS :";Q$
200 FOR T=1 TO 30*S:NEXT T
210 GOTO 90
220 FOR J=1 TO LEN(F$)
230 LET W$=MID$(F$,J,1)
240 IF W$="." THEN LET K=1
250 IF W$="-" THEN LET K=3
260 GOSUB 330: LET K=1
270 GOSUB 340
280 NEXT J
290 RETURN
300 PRINT
310 LET Q$=CHR$(INT(RND(1)*26+65))
320 RETURN
330 PRINT TAB(10,10);"*"
340 FOR T=1 TO P*K:NEXT T
350 PRINT TAB(10,10);" "
360 RETURN
"""

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Morse Coder",sys.modules[__name__])