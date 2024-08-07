#!/usr/bin/env python3

import loader
import sys
import util
import math
from random import randint

"""
Title: Rendezvous
Author: Jenny Tyler & Chris Oxlade
Translator: David Sarkies
Version: 0.0
Date: 31 July 2024
Source: https://archive.org/details/Computer_Spy_Games
This game can be found on page 12 of Computer Spy Games, and it a python3 translation.

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

commands = "Commands\n========\n\n"
commands = "{}TIME: Tells you what time it is.\n".format(commands)
commands = "{}MOVE: Ask you where to. You can go anywhere marked on the map.\n".format(commands)
commands = "{}SAY: The password.\n".format(commands)
commands = "{}EXAMINE: Anything. (Examine the key to get the number).\n".format(commands)
commands = "{}READ: A message.\n".format(commands)
commands = "{}OPEN: The locker.\n".format(commands)
commands = "{}FOLLOW: An enemy Spy.\n".format(commands)
commands = "{}WAIT: for any length of time.\n".format(commands)
commands = "{}LEAVE: A message.\n".format(commands)
commands = "{}SEARCH: Anywhere (to find the key).\n".format(commands)
commands = "{}HELP: Reminds you of the time and places of the meeting.\n".format(commands)
commands = "{}COMMANDS: Displays the commands available to you.\n".format(commands)
commands = "{}MAP: Lists the locations on the map.\n".format(commands)
commands = "{}QUIT: Ends the game\n\n".format(commands)
commands = "{}You can also use any of the names on the map.\n\n".format(commands)

locations = ["Airport","Bus Stop","Bridge","Canal","Church","Park","Cafe","Bank","Cinema","Hotel",
			 "Casino","Town Square","Post Office","Police Station","Fairground","Station","Town Hall",
			 "Embassy","Gardens","Castle"]
actions = ["MOVE","SAY","EXAMINE","READ","OPEN","FOLLOW","WAIT","LEAVE","SEARCH","TIME","HELP","COMMANDS","MAP",
			"QUIT"]
passwords = ["CUSTARD","KIPPER","KOALA","CRUMPET","CROSSWORD","KANGAROO"]
game_header = "Redezvous\n========="

def display_commands():
	print(commands)

def display_locations():

	location_list = ""

	for x in locations:
		location_list = "{}{}\n".format(location_list,x)

	print(location_list)

def random_number(end,start=0):

	return randint(start,end)

def game_routine():

	hour = random_number(10,8)
	minute = 0
	flightHour = random_number(16,14)
	contactTime = random_number(hour,2)
	locker_number = random_number(999,900)

	messagePlace = random_number(18)
	keyPlace = random_number(18)
	enemyPlace = random_number(18)
	contactPlace = random_number(18)
	password = passwords[random_number(5)]
	haveMessage = False #flag 1
	messageLeft = False #flag 2
	contact_met = False #flag 3
	flag4 = 0
	haveKey = False #Flag 5
	haveCase = False #Flag 6
	caseGiven = False #Flag 7

	game_condition = 0
	player_position = 1
	enemy_position = 10
	near_enemy = 0
	player_x = 0
	player_y = 0
	num_moves = 0
	player_message = ""
	meeting_time = 0
	meeting_place = -1
	
	display_task(messagePlace,contactPlace,contactTime,flightHour)

	while (game_condition == 0):
		
		near_enemy = display_location(player_position,enemy_position,near_enemy,messagePlace,haveMessage)
		num_moves +=1
		contactMet = False

		print(player_message)
		player_message = ""

		#Is the player with the contact
		time = hour+(minute/100)
		meeting_end = meeting_time + 0.15
		if ((flag4 == 1) and (player_position == meeting_place) and (meeting_time<=time) and (meeting_end>=time)):
			print("Contact is here")
			contactMet = True

		if ((player_position == 1) and (hour<flightHour) and (caseGiven == True)):
			game_condition = 1
		else:
			request = get_input("\nWhat Next: ",actions,"I'm sorry, I don't understand")

			#Are you spotted by the enemy agent
			spotted = random_number(10)
			if ((near_enemy==3) and (spotted>3) and (request != 0)):
				player_message = "The Enemy Agent Sees You"
			elif (near_enemy ==4):
				game_condition = 2
			else:

				time_taken = 0

				#Move
				if (request == 0):
					new_position = move()
					player_x,player_y,time_taken = calculate_time(new_position,player_x,player_y)
					player_position = new_position

				#Speak
				elif (request == 1):
					time_taken = 5
					player_message,success = speak(enemy_position,player_position,contact_met,haveCase,password)

				#Examine
				elif (request == 2):
					time_taken = 5
					player_message = examine(haveCase,haveKey,locker_number)

				#Read
				elif (request == 3):
					player_message = read(haveMessage,messagePlace,player_position,password)

				#Open
				elif (request == 4):
					time_taken = 5
					player_message,haveCase = open_command(player_position,haveKey,locker_number)

				#Follow
				elif (request == 5):
					
					player_message,player_position,enemy_position,player_x,player_y,time_taken = follow(
						player_position,enemy_position,player_x,player_y,keyPlace)

				#Wait
				elif (request == 6):
					time_taken = wait()

				#Leave
				elif (request == 7):
					messageLeft,messagePlace,meeting_time = leave_message(
						player_position,contactPlace,contactTime,hour)
				#Map
				elif (request == 11):
					display_commands()
					input("Press Enter")

				#Locations
				elif (request == 12):
					display_locations()
					input("Press Enter")

				#Quit
				elif (request == 13):
					game_condition = 3

				#Updates the current time
				minute += time_taken
				while (minute>59):
					minute -= 60
					hour += 1

	if (game_condition == 2):
		print("You have been captured.")


"""
300 ON V GOSUB 360,420,540,570,640,710,730,780,810,820,870

320 IF F(2)=1 ANF H>=CH THEN LET F(4)=1
330 IF H=FJ THEN GOTO 880
340 IF FNA(10)>9 THEN LET EP=10
350 GOTO 70



730 PRINT:PRINT "WHERE DO YOU WANT TO MEET":INPUT S$
740 PRINT:PRINT "WHAT TIME (HH.MM)"
750 INPUT U
760 IF P=CP AND T1<U AND H<CH THEN LET F(2)=1
770 LET DT=5:RETURN


"""

def leave_message(player_position,contactPlace,contactTime,hour):

	correct = False
	meeting_place = -1


	#Gets location of meeting and checks if it is a valid location
	while (not correct):

		suggested_place = input("Where do you want to meet: ")
		place_count = 0

		for x in locations:
			if (suggested_place.upper() == x.upper()):
				correct = True
				meeting_place = place_count
			else:
				place_count +=1

		if (not correct):
			print("Sorry, I don't know that place")

	correct = False

	#Asks for hour to meet (between 0 and 23)
	#Asks for minute (between 0 and 59)
	#

def wait():

	time_taken = util.get_num_input("How many minutes ",1,10000)

	return time_taken

def follow(player_position,enemy_position,player_x,player_y,keyPlace):

	player_message = ""
	time_taken = 0

	if (enemy_position != player_position):
		player_message = "Follow Who?"
		time_taken = 5
	else:
		new_position = random_number(20)
		player_x,player_y,time_taken = calculate_time(new_position,player_x,player_y)
		player_position = new_position

		random_follow = random_number(10)

		if (random_follow>7):
	
			player_message = "You lost him after a while"

			if (random_follow>8):
				player_position = keyPlace
		else:
			player_message = "You kept him in sight."
			enemy_position = player_position

	return player_message,player_position,enemy_position,player_x,player_y,time_taken

def open_command(player_position,haveKey,locker_number):

	haveCase = False
	player_message = ""

	if (player_position != 16):
		player_message = "Nothing to open"
	elif (not haveKey):
		player_message = "You have no key"
	else:
		number = input("What number locker: ")

		if number != str(locker_number):
			player_message = "The key does not fit"
		else:
			player_message = "Locker is open - you have the case"
			haveCase = True

	return player_message,haveCase

def read(haveMessage,messagePlace,player_position,password):

	player_message = "Nothing to read."

	if ((player_position == messagePlace) or (haveMessage == True)):
		player_message = "A Word: '{}'".format(password)
		haveMessage = True

	return player_message,haveMessage


def examine(haveCase,haveKey,locker_number):

	object_examined = input("What do you want to examine: ")
	player_message = ""

	if ((object_examined.upper() == "CASE") and (haveCase)):
		player_message = "Top secret!"
	elif ((object_examined.upper() == "KEY") and (haveKey)):
		player_message = "A number: {}".format(locker_number)
	else:
		player_message = "Nothing Specials"

	return player_message

def speak(enemy_position,player_position,contact_met,haveCase,password):

	player_message = ""
	success = False
	word_spoken = input("\nSay What: ")

	if (enemy_position == player_position):
		player_message = "You attracted the enemy agent!"
	elif (contact_met == False):
		player_message = "Nobody hears you"
	elif (word_spoken.upper() != password.upper()):
		player_message = "Contact ignores you"
	elif (haveCase == True):
		player_message = "You made contact - he takes the case"
		success = True
	else:
		player_message = "'{}'".format(word_spoken) 

	return player_message,success

def move():

	return get_input("\nWhere To: ",locations,"I don't know that place")

#Calculates the time to move to a new place
def calculate_time(new_position,player_x,player_y):

	new_y = int((new_position-1)/5)
	new_x = new_position-5*new_y
	dx = abs(player_x-new_x)
	dy = abs(player_y-new_y)
	d = math.sqrt((dx*dx)+(dy*dy))
	time_taken = int(5*d)

	return new_x,new_y,time_taken

#Retrieves player command
def get_input(query,actions,error):

	correct = False

	#Validation loop
	while(not correct):

		#Requests player input
		request = input(query)
		command = 0
		action_number = -1

		#Cycles through commands and locates what player typed
		while(command<len(actions)):

			if ((request.upper() == actions[command].upper())):
				action_number = command
			command += 1

		#No such command exists
		if (action_number==-1):
			print(error)
		else:
			correct = True

	return action_number


def display_location(player_position,enemy_position,near_enemy,messagePlace,haveMessage):

	#util.clear_screen()
	print(game_header)
	print("\nYou are at the {}".format(locations[player_position]))

	if (enemy_position == player_position):
		print("The enemy agent is here")
		near_enemy += 1
	else:
		near_enemy = 0

	if ((player_position == messagePlace) and (haveMessage == False)):
		print("Message for you here")

	return near_enemy

def display_task(message,contactPlace,contactTime,flightTime):
	
	print(game_header)
	print("\nCollect the message from the {}".format(locations[message]))
	print("Contact will collect from the {} at {}.00".format(locations[contactPlace],contactTime))
	print("The last flight leaves at {}.00\n".format(flightTime))
	input("Press return to continue.")

def main_game():

	util.clear_screen()
	print("Do you want a list of commands?")
	response = util.yes_or_no("")

	if (response):
		display_commands()

	print("Do you want a list of locations?")
	response = util.yes_or_no("")

	if(response):
		util.clear_screen()
		print("Locations\n=========")
		display_locations()
	
	util.clear_screen()
	game_routine()

"""






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







#1010 DIM R$(20),V$(11),F(7)
#1020 FOR I=1 TO 20:READ R$(I)
#1030 NEXT I
#1040 FOR I=1 TO 11:READ V$(I):NEXT I
#1050 RETURN
#1060 DATA "AIRPORT","BUS STOP","BRIDGE","CANAL","CHURCH"
#1070 DATA "PARK","CAFE","BANK","CINEMA","HOTEL"
#1080 DATA "CASINO","TOWN SQUARE","POST OFFICE","POLICE STATION","FAIRGROUND"
#1090 DATA "STATION","TOWN HALL","EMBASSY","GARDENS","CASTLE"
#1100 DATA "MOVE","SAY","EXAMINE","READ","OPEN","FOLLOW","WAIT","LEAVE","SEARCH"
#1110 DATA "TIME","HELP"
#1120 DATA "CUSTARD","KIPPER","KOALA","CRUMPET","CROSSWORD","KANGAROO"
#1130 LET H=FNA(2)+8:LET M=0
#1140 LEF FH=FNA(2)+14
#1150 LET CH=FNA(2)+H
#1160 CLS:PRINT:PRINT
#1170 LET NE=0:LET T$="CONTACT IS HERE"
#1180 LET MP=FNA(18):LET KP=FNA(18)
#1190 LET EP=FNA(18):LET CP=FNA(18)
#1200 FOR I=1 TO FNA(6)
#1210 READ P$:NEXT I
#1220 LET NL=FNA(900)+99
#1230 PRINT "RENDEZVOUS"
#1240 PRINT "==========":PRINT
#1250 PRINT "COLLECT MESSAGE FROM"
#1260 PRINT "THE ";R$(MP)
#1270 PRINT "CONTACT WILL COLLECT"
#1280 PRINT "FROM TEH ";R$(CP)
#1290 PRINT "AT ";CH;".00"
#1300 PRINT "LAST FLIGHT LEAVES"
#1310 PRINT "AT ";FH;".00"
#1320 PRINT:PRINT "PRESS RETURN TO CONTINUE"
#1330 INPUT Q$:RETURN
"""

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Spy Eyes",sys.modules[__name__])