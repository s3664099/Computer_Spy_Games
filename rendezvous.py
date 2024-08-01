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
This game can be found on page {} of Computer Spy Games, and it a python3 translation.

"""

instructions = "Your mission is a complicated one, so read these instructions\n"
instructions = "{}carefully.\n".format(instructions)
instructions = "{}You must collect a case from a locker at the station, hand it\n".format(instructions)
instructions = "{}over to your contact and get back to the airport before the last\n".format(instructions)
instructions = "{}plane takes off (your computer will tell you what time this is).\n".format(instructions)
instructions = "{}Your computer will tell you where your contact will be at what\n".format(instructions)
instructions = "{}time. You must leave a message at that place, before he gets\n".format(instructions)
instructions = "{}there, telling him where and when you will meet him and hand\n".format(instructions)
instructions = "{}over the case.\n".format(instructions)
instructions = "{}You must find out the password before you meet him, and make sure\n".format(instructions)
instructions = "{}you are not more than 15 minutes late.\n".format(instructions)
instructions = "{}Before you can get the case, you must find the key to the locker\n".format(instructions)
instructions = "{}and also its number. Unfortunately the key is in the hands of\n".format(instructions)
instructions = "{}enemy agenst. whose HQ is at the Hotel. You must find an enemy\n".format(instructions)
instructions = "{}spy and follow him, hoping he will be careless enough to drop\n".format(instructions)
instructions = "{}the key (and of course that he won't see you).\n".format(instructions)
instructions = "{}The map shows you the places you can go to and the lest below\n".format(instructions)
instructions = "{}shows the words you can use in the game".format(instructions)

#instructions = "{}{}".format(instructions,commands)

#commands = "Commands\n========\n\n"
#commands = ""


def main_game():
	
	print("Main Game")

"""
10 DEF FNA(X)=INT(RND(1)*X)+1
20 GOSUB 1010:GOSUB 1130
30 LET P=1:LET Y=0:LET X=1:LET EP=10
40 LET U=0:LET NM=0
50 LET S$=""
60 LET B$=""
70 CLS:PRINT:PRINT "RENDEZVOUS"
80 PRINT "=========="
90 LET NM=NM+1
100 PRINT:PRINT
110 PRINT B$:PRINT
120 PRINT:PRINT "YOU ARE AT THE ";
130 PRINT R$(P)
140 IF EP=P THEN PRINT "ENEMY AGENT IS HERE": LET NE=NE+1
150 IF EP<>P THEN LET NE=0
160 IF P=MP AND F(1)=0 THEN PRINT "MESSAGE FOR YOU HERE"
170 LET F(3)=0
180 LET T1=H+M/100
190 IF F(4)=1 AND R$(P)=S$ AND U<=T1 AND U+.15>T1 THEN PRINT T$:LET F(3)=1
200 IF P=1 AND H<FH AND F(7)=1 THEN GOTO 890
210 PRINT:PRINT:PRINT "WHAT NEXT"
220 LET B$=""
230 INPUT I$
240 LET V=0:FOR I=1 TO 11
250 IF I$=V$(I) THEN LET V=1
260 NEXT I
270 IF V=0 THEN LET V=12
280 IF NE=3 AND FNA(10)>3 AND V<>1 THEN LET B$="ENEMY AGENT SEES YOU!":GOTO 70
290 IF NE=4 THNE PRINT "YOU ARE CAPTURED":STOP
300 ON V GOSUB 360,420,540,570,640,710,730,780,810,820,870
310 LET M=M+DT:IF M>59 THEN LET M=M-60:LET H=H+1
320 IF F(2)=1 ANF H>=CH THEN LET F(4)=1
330 IF H=FJ THEN GOTO 880
340 IF FNA(10)>9 THEN LET EP=10
350 GOTO 70
360 PRINT:PRINT "WHERE TO":INPUT N$
370 LET NP=0:FOR I=1 TO 20
380 IF N$=R$(I) THEN LET NP=I
390 NEXT I:IF NP=0 THE GOTO 360
400 GOSUB 950
410 LET P=NP:RETURN
420 LET DT=5
430 PRINT:PRINT "SAY WHAT":INPUT Q$
440 IF EP=P THEN LET B$="YOU ATTRACTED THE ENEMY AGENT!":RETURN
450 IF F(3)=0 THEN LET B$="NOBODY HEARS YOU":RETURN
460 IF Q$<>P$ THEN LET B$="CONTACT IGNORES YOU!":RETURN
470 IF F(6)=1 TREN LET B$="YOU MADE CONTACT - HE TAKES THE CASE!"
480 LET F(7)=1:RETURN
490 LET DT=5
500 PRINT "WHAT DO YOU WANT TO EXAMINE":INPUT Q$
510 IF Q$="CASE" THEN LET B$="TOP SECRET!":RETURN
520 IF Q$="KEY" THEN LET B$="a NUMBER = "+STR$(NL):RETURN
530 LET B$="NOTHING SPECIAL!":RETURN
540 IF P<>MP OR F(1)=1 THEN LET B$="NOTHING TO READ!":RETURN
550 LET B$="A WORD - '"+P$+"'"
560 LET F(1)=1:RETURN
570 LET DT=5
580 IF P<>16 THEN LET B$="NOTHING TO OPEN":RETURN
590 IF F(5)=0 THEN LET B$="YOU HAVE NO KEY":RETURN
600 PRINT:PRINT "WHAT NUMBER LOCKER":INPUT YN
610 IF NL<>YN THEN LET B$="THE KEY DOES NOT FIT":RETURN
620 LET B$="LOCKER IS OPEN - YOU HAVE THE CASE!":LET F(6)=1
630 RETURN
640 LET DT=5
650 IF EP<>P THEN LET B$="FOLLOW WHO?":RETURN
660 LET NP=FNA(20):GOSUB 950:LET P=NP
670 IF FNA(10)>8 THEN LET P=KP
680 IF FNA(10)>7 THEN B$="YOU LOST HIM AFTER A WHILE!":RETURN
690 LET EP=P
700 LET B$="YOU KEPT HIM IN SIGHT":RETURN
710 PRINT:PRINT "HOW MANY MINUTES":INPUT S$
720 RETURN
730 PRINT:PRINT "WHERE DO YOU WANT TO MEET":INPUT S$
740 PRINT:PRINT "WHAT TIME (HH.MM)"
750 INPUT U
760 IF P=CP AND T1<U AND H<CH THEN LET F(2)=1
770 LET DT=5:RETURN
780 LET B$="NOTHING HERE":LET DT=10
790 IF P=KP THEN LET B$="YOU FOUND A KEY":LET F(5)=1
800 RETURN
810 LET DT=0:LET B$="TIME IS NOW "+STR$(H)+"."+STR$(M):RETURN
820 LET DT=5
830 IF U=0 THEN GOTO 860
840 PRINT:PRINT "MEETING PLACE IS"
850 PRINT S$;" AT ";U
860 GOSUB 1300:RETURN
870 LET DT=0:LET B$="PARDON?":RETURN
880 PRINT "TOO LATE ":STOP
890 PRINT:PRINT "WELL DONE, YOUR MISSING WAS A SUCCESS!"
900 LET TL=(FH-H)*60-M
910 LET S=INT((20/NM+TL/120)*50)
920 PRINT:PRINT "YOUR SPY RATING"
930 PRINT "IS ";S
940 STOP
950 LET NY=INT((NP-1)/5)
960 LET NX=NP-5*NY
970 LET DX=ABS(X-NI):LET DY=ABS(Y-NY)
980 LET X=NX:LET Y=NY
990 LET D=SQR(DX^2+DY^2)
1000 LET DT=INT(5*D):RETURN
1010 DIM R$(20),V$(11),F(7)
1020 FOR I=1 TO 20:READ R$(I)
1030 NEXT I
1040 FOR I=1 TO 11:READ V$(I):NEXT I
1050 RETURN
1060 DATA "AIRPORT","BUS STOP","BRIDGE","CANAL","CHURCH"
1070 DATA "PARK","CAFE","BANK","CINEMA","HOTEL"
1080 DATA "CASINO","TOWN SQUARE","POST OFFICE","POLICE STATION","FAIRGROUND"
1090 DATA "STATION","TOWN HALL","EMBASSY","GARDENS","CASTLE"
1100 DATA "MOVE","SAY","EXAMINE","READ","OPEN","FOLLOW","WAIT","LEAVE","SEARCH"
1110 DATA "TIME","HELP"
1120 DATA "CUSTARD","KIPPER","KOALA","CRUMPET","CROSSWORD","KANGAROO"
1130 LET H=FNA(2)+8:LET M=0
1140 LEF FH=FNA(2)+14
1150 LET CH=FNA(2)+H
1160 CLS:PRINT:PRINT
1170 LET NE=0:LET T$="CONTACT IS HERE"
1180 LET MP=FNA(18):LET KP=FNA(18)
1190 LET EP=FNA(18):LET CP=FNA(18)
1200 FOR I=1 TO FNA(6)
1210 READ P$:NEXT I
1220 LET NL=FNA(900)+99
1230 PRINT "RENDEZVOUS"
1240 PRINT "==========":PRINT
1250 PRINT "COLLECT MESSAGE FROM"
1260 PRINT "THE ";R$(MP)
1270 PRINT "CONTACT WILL COLLECT"
1280 PRINT "FROM TEH ";R$(CP)
1290 PRINT "AT ";CH;".00"
1300 PRINT "LAST FLIGHT LEAVES"
1310 PRINT "AT ";FH;".00"
1320 PRINT:PRINT "PRESS RETURN TO CONTINUE"
1330 INPUT Q$:RETURN
"""

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Spy Eyes",sys.modules[__name__])