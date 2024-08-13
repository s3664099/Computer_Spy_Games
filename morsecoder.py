#!/usr/bin/env python3

import loader
import sys
import util
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

instructions = "If you want to be a really successful spy, you need to\n"
instructions = "{}know how to send, recieve and, of course, intercept\n".format(instructions)
instructions = "{}messages in Morse Code. This program will help you\n".format(instructions)
instructions = "{}learn. If you have never used Morse Code before, you\n".format(instructions)
instructions = "{}will need to make yourself a chart of letters and their\n",format(instructions)
instructions = "{}Morse equivalents. Use lines 400-450 of the program to\n".format(instructions)
instructions = "{}do this. They show the Morse code for each letter of the\n".format(instructions)
instructions = "{}alphabet in order.\n".format(instructions)
instructions = "{}\nWhat you have to do\n\n".format(instructions)
instructions = "{}In Morse Code, each letter is represented by a series of\n".format(instructions)
instructions = "{}long and short sounds or flashes. This program uses a\n".format(instructions)
instructions = "{}flashing star. it will give you the code for a letter and\n".format(instructions)
instructions = "{}then ask you which it was. You will have to watch carefully\n".format(instructions)
instructions = "{}to pick out the long and short flashes and remember them.\n".format(instructions)
instructions = "{}You will see the cursor flashing too at the left of the screen.\n".format(instructions)
instructions = "{}Ignore this it has nothing to do with the code.".format(instructions)


def main_game():
	
	print("Main Game")

"""
10 GOSUB 370
20 CLS
30 LET S=30
40 PRINT:PRINT "MORSE TESTER"
50 PRINT:PRINT "WHAT LEVEL?"
60 PRINT:PRINT "(1=FAST)"
70 PRINT:PRINT "(5=SLOW)"
80 INPUT P:LET P=P*S
90 CLS
100 PRINT:PRINT "GET READY"
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
370 DIM M$(26)
380 FOR I=1 TO 26:READ M$(I):NEXT I
390 RETURN
400 DATA ".-","-...","-.-","-..","."
410 DATA "..-","--.","....","..",".---"
420 DATA "-.-",".-..","--","-.","---"
430 DATA ".--","--.-",".-.","...","-"
440 DATA "..-","...-",".--","-..-"
450 DATA "-.--","--.."

"""

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Morse Coder",sys.modules[__name__])