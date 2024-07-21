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
	
	print("Main Game")

"""
10 CLS:PRINT:PRINT "SECRET MESSAGE MAKER"
20 PRINT "===================="
30 PRINT:PRINT "DO YOU WANT TO:"
40 PRINT
50 PRINT "   1. CODE A MESSAGE"
60 PRINT "OR 2. DECODE A MESSAGE"
70 PRINT:PRINT
80 PRINT "ENTER NUMBER":INPUT A
90 IF A=1 THEN GOSUB 120
100 IF A=2 THE GOSUB 210
110 GOTO 30
120 LET C$="CODED":GOSUB 400
130 LET X=INT(RND(1)*25+1)
140 LET M$="F"+M$
150 GOSUB 310:GOSUB 420
160 LET M$=CHR$(X+64)+M$
170 IF LEN(M$)/2=INT(LEN(M$)/2) THEN GOSUB 450
180 PRINT "THE CODED MESSAGE IS":
190 PRINT M$
200 RETURN
210 LET C$="DECODED":GOSUB 400
220 IF LEN(M$)/2=INT(LEN(M$)/2) THEN GOSUB 450
230 LET K$=LEFT$(M$,1)
240 LET M$=RIGHT$(M$,LEN(M$)-1)
250 LET X=ASC(K$)-64
260 LET X=-X:GOSUB 420
270 GOSUB 310:M$=RIGHT$(M$,LEN(M$)-1)
280 PRINT "THE DECODED MESSAGE IS:"
290 PRINT M$
300 RETURN
310 LET N$=""
320 FOR I=1 TO LEN(M$)
330 LET Q$=MID$(M$,I,1):LET N=ASC(Q$)
340 IF N=32 THEN GOTO 380
350 LET N=N+X
360 IF N>90 THEN LET N=N-26
370 IF N<65 THEN LET N=N+26
380 LET N$=N$+CHR$(N):NEXT I
390 LET M$=N$:RETURN
400 PRINT "WHAT IS THE MESSAGE TO BE ";C$
410 INPUT M$:RETURN
420 LET N$="":FOR I=LEN(M$) TO 1 STEP -1:NEXT I
430 LET N$=N$+MID$(M$,I,1):NEXT I
440 LET M$=N$:RETURN
450 LET N$="":LET L=LEN(M$)
460 FOR I=1 TO LEN(M$)-1 STEP 2
470 LET N$=N$+MID$(M$,I+1,1)
480 LET N$=N$+MID$(M$,I,1)
490 NEXT I:LET M$=N$:RETURN
"""

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Spy Eyes",sys.modules[__name__])