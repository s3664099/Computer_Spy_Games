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
Version: 2.0
Date: 11 August 2024
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
instructions = "{}enemy agent. whose HQ is at the Hotel. You must find an enemy\n".format(instructions)
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

def main_game():

	playing = True

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

	while(playing):
		game_routine()
		playing = util.play_again(playing)

def game_routine():

	hour = random_number(10,8)
	minute = 0
	flightHour = random_number(16,14)
	contactTime = random_number(hour+2,hour+1)
	locker_number = random_number(999,900)

	messagePlace = random_number(18)
	keyPlace = random_number(18)
	enemyPlace = random_number(18)
	contactPlace = random_number(18)
	password = passwords[random_number(5)]
	haveMessage = False #flag 1
	messageLeft = False #flag 2
	contact_met = False #flag 3
	messageRecieve = False #flag 4
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
		contact_met = False

		print(player_message)
		player_message = ""

		#Is the player with the contact
		time = hour+(minute/100)
		meeting_end = meeting_time + 0.15
		if ((messageRecieve) and (player_position == meeting_place) and (meeting_time<=time) and (meeting_end>=time)):
			print("Contact is here")
			contact_met = True

		if ((player_position == 0) and (hour<flightHour) and (caseGiven == True)):
			game_condition = 1
		elif (hour >= flightHour):
			game_condition = 4
		else:
			command = get_input("\nWhat Next: ",actions,"I'm sorry, I don't understand",True)
			request = command[0]

			#Are you spotted by the enemy agent
			spotted = random_number(10)
			if ((near_enemy==3) and (spotted>3) and (request != 0)):
				player_message = "The Enemy Agent Sees You"
			elif ((near_enemy ==4) and (request !=0)):
				game_condition = 2
			else:

				time_taken = 0

				#Move
				if (request == 0):
					new_position = move(command[1])
					player_x,player_y,time_taken = calculate_time(new_position,player_x,player_y)
					player_position = new_position

				#Speak
				elif (request == 1):
					time_taken = 5
					player_message,caseGiven = speak(enemy_position,player_position,contact_met,haveCase,
						password,command[1])

				#Examine
				elif (request == 2):
					time_taken = 5
					player_message = examine(haveCase,haveKey,locker_number,command[1])

				#Read
				elif (request == 3):
					player_message,haveMessage = read(haveMessage,messagePlace,player_position,password,command[1])

				#Open
				elif (request == 4):
					time_taken = 5
					player_message,haveCase = open_command(player_position,haveKey,locker_number,command[1])

				#Follow
				elif (request == 5):
					
					player_message,player_position,enemy_position,player_x,player_y,time_taken = follow(
						player_position,enemy_position,player_x,player_y,keyPlace)

				#Wait
				elif (request == 6):
					time_taken = wait()

				#Leave
				elif (request == 7):
					time_taken = 5
					messageLeft,meeting_place,meeting_time = leave_message(
						player_position,contactPlace,contactTime,hour,time)
				#Search
				elif (request == 8):
					time_taken = 10
					player_message,haveKey = search(player_position,keyPlace)

				#Get Time
				elif (request == 9):
					player_message  = get_time(hour,minute)

				#Help
				elif (request == 10):
					help(meeting_place,meeting_time,flightHour)

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

				else:
					player_message = "Pardon?"

				#Updates the current time
				minute += time_taken

				while (minute>59):
					minute -= 60
					hour += 1

				if ((messageLeft) and (hour>contactTime)):
					messageRecieve = True

				if (random_number(10)>9):
					enemy_position = 10

	if (game_condition == 2):
		print("You have been captured.")
	elif (game_condition == 4):
		print("Too late - you missed the last flight")
	elif (game_condition == 1):
		print("Well done, your mission was a success!")
		time_left = (flightHour - hour) * 60 - minute
		score = int((20/num_moves)+(time_left/120)*50)
		print("Your Spy Rating is: {}".format(score))

def help(meeting_place,meeting_time,flightTime):

	if (meeting_time != 0):

		meeting_time = str(meeting_time).split(".")

		if (len(meeting_time[1])<0):
			meeting_time[1]="0{}".format(meeting_time[1])

		print("\nThe Meeting Place is {} at {}:{}.".format(locations[meeting_place],meeting_time[0],meeting_time[1]))

	print("The last flight leaves at {}:00\n".format(flightTime))
	input("Press return to continue.")

def get_time(hour,minute):

	if (minute<10):
		minute = "0{}".format(minute)

	return "The time is now {}:{}".format(hour,minute)

def search(player_position,keyPlace):

	player_message = "Nothing here"
	haveKey = False

	if (player_position == keyPlace):
		player_message = "You found a key"
		haveKey = True

	return player_message,haveKey

def leave_message(player_position,contactPlace,contactTime,hour,time):

	correct = False
	meeting_place = -1
	meeting_time = 0
	messageLeft = False

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

	contact_hour = util.get_num_input("What Hour ",0,23)
	contact_minute = util.get_num_input("What Minute ",0,59)
	meeting_time = contact_hour+(contact_minute/100)

	if ((player_position == contactPlace) and (time<contactTime) and (hour<contactTime)):
		messageLeft = True

	return messageLeft,meeting_place,meeting_time

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
		new_position = random_number(len(locations)-1)
		player_x,player_y,time_taken = calculate_time(new_position,player_x,player_y)
		player_position = new_position

		if (random_number(10)>8):
				player_position = keyPlace

		if (random_number(10)>7):
			player_message = "You lost him after a while"
		else:
			player_message = "You kept him in sight."
			enemy_position = player_position

	return player_message,player_position,enemy_position,player_x,player_y,time_taken

def open_command(player_position,haveKey,locker_number,number):

	haveCase = False
	player_message = ""

	if (player_position != 15):
		player_message = "Nothing to open"
	elif (not haveKey):
		player_message = "You have no key"
	else:

		if (number==""):
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


def examine(haveCase,haveKey,locker_number,object_examined):

	if (object_examined==""):
		object_examined = input("What do you want to examine: ")

	player_message = ""

	if ((object_examined.upper() == "CASE") and (haveCase)):
		player_message = "Top secret!"
	elif ((object_examined.upper() == "KEY") and (haveKey)):
		player_message = "A number: {}".format(locker_number)
	else:
		player_message = "Nothing Special"

	return player_message

def speak(enemy_position,player_position,contact_met,haveCase,password,word_spoken):

	player_message = ""
	success = False

	if (word_spoken==""):
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

def move(place):

	new_place = -1

	if (len(place)>0):

		command = 0

		#Cycles through commands and locates what player typed
		while(command<len(locations)):

			if ((place.upper() == locations[command].upper())):
				new_place = command
			command += 1

		#No such command exists
		if (new_place==-1):
			print(error)
	else:
		new_place = get_input("\nWhere To: ",locations,"I don't know that place")

	return new_place

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
def get_input(query,actions,error,main_input = False):

	correct = False

	#Validation loop
	while(not correct):

		#Requests player input
		request = input(query)
		command = 0
		action_number = -1
		subject = ""

		#Checks if it is the main input and allows for multiple words
		if (main_input):
			commands = request.split(" ")
			
			if (len(commands)>1):
				subject = request[len(commands[0]):].strip()
			request = commands[0]

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

		if(main_input):
			action_number = [action_number,subject]

	return action_number


def display_location(player_position,enemy_position,near_enemy,messagePlace,haveMessage):

	util.clear_screen()
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

def display_commands():
	print(commands)

def display_locations():

	location_list = ""

	for x in locations:
		location_list = "{}{}\n".format(location_list,x)

	print(location_list)

def random_number(end,start=0):
	return randint(start,end)

#Passes the current file as a module to the loader
if __name__ == '__main__':
	loader.start_game("Rendezvous",sys.modules[__name__])