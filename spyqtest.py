#!/usr/bin/env python3

import loader
import sys
import util
from random import randint

"""
Title: Spy-Q Test
Author: Jenny Tyler & Chris Oxlade
Translator: David Sarkies
Version: 0.1
Date: 17 July 2024
Source: https://archive.org/details/Computer_Spy_Games
This game can be found on page 8 of Computer Spy Games, and it a python3 translation.

"""

instructions = ""

def main_game():
	
	print("Main Game")

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Spy Eyes",sys.modules[__name__])

"""
10 DIM N(10):DIM N$(5)
20 CLS
30 GOSUB 510
50 LET W$=""
50 LET D=5
60 LET G=0
70 FOR I=1 TO 10:LET N(I)=0:NEXT I
80 LET I=1
90 GOSUB 430
100 LET M=INT(RND(1)*99+1)
110 PRINT:PRINT "WHERE WILL YOU PUT ";M
120 PRINT:INPUT P$
130 IF P$="D" AND G<D THEN LET G=G+1:GOTO 90
140 IF P$="D" THEN PRINT "YOU CAN'T!":GOTO 120
150 LET P=VAL(P$)
160 IF P<1 OR P>10 THEN GOTO 120
170 IF N(P)>0 THEN PRINT "ALREADY FULL":GOTO 120
180 LET N(P)=M
190 LET F=0
200 FOR L=P TO 10
210 IF N(L)<M AND N(L)<>0 THEN LET F=1
220 NEXT L
230 FOR L=1 TO P
240 IF N(L)>M AND N(L)<>0 THEN LET F=1
250 NEXT L
260 IF F=1 THEN GOTO 360
270 LET I=I+1:IF I<11 THEN GOTO 90
280 LET D=D-1:IF D=0 THEN GOTO 330
290 PRINT "WELL DONE, GO TO GRADE ";D
300 PRINT:PRINT "YOU ARE NOW A ";N$(D)
310 LET W$=""
320 GOTO 400
330 PRINT "TERRIFIC - YOU HAVE REACHED"
340 PRINT "THE GRADE OF SUPER SPY"
350 STOP
360 PRINT "WRONG! NOT GOOD ENOUGH"
370 PRINT N$(D)
390 LET W$="STILL"
400 PRINT:PRINT "DO YOU WANT TO TRY AGAIN? (Y/N)"
410 INPUT A$:IF A$="Y" THEN GOTO 60
420 STOP
430 CLS
440 PRINT:PRINT "YOU ARE ";W$;" A ";N$(D)
450 PRINT
460 FOR J=1 TO 10
470 PRINT J;
480 IF N(J)>0 THEN PRINT N(J);
490 PRINT:NEXT J
500 RETURN
510 FOR I=1 TO 5:READ N$(I)
520 NEXT I
530 RETURN
540 DATA "VIS","SPY","JUNIOR SPY"
550 DATA "SPYING ASSISTANT","TRAINEE SPY"
"""