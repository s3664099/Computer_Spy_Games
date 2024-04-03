"""
Title: Graphics Package for Searchlight
Translator: David Sarkies
Version: 1
Date: 2 April 2023

This file holds a series of functions that enable graphical displays using pygame.

To install pygame you need to do the following:

pip3 install pygame
"""

import pygame

cell_size = 50
columns = 20
rows = 15
searchlight_column = 10
display_width = cell_size * columns
display_height = cell_size * rows
player = pygame.transform.scale(pygame.image.load("icons/spy.png"),(cell_size,cell_size))
rock = pygame.transform.scale(pygame.image.load("icons/rocks.png"),(cell_size,cell_size))
building = pygame.transform.scale(pygame.image.load("icons/building.png"),(cell_size,cell_size))
tree = pygame.transform.scale(pygame.image.load("icons/tree.png"),(cell_size,cell_size))
spotlight = pygame.transform.scale(pygame.image.load("icons/spotlight.png"),(cell_size,cell_size))
white = (255,255,255)

def display_screen():

	gameDisplay = pygame.display.set_mode((display_width,display_height))
	return gameDisplay

#Sets the caption of the screen
def set_caption(title):
	pygame.display.set_caption(title)

def clear_screen(display):

	display.fill((0, 0, 0))

	return display

def update_display(display):

	pygame.display.update()

#Functions to display elements on the map
def display_map(map_level,display,row):

	for x in range(len(map_level)):

		if map_level[x] == "0":
			display.blit(rock, (x*cell_size,row*cell_size))
		elif map_level[x] == "1":
			display.blit(tree, (x*cell_size,row*cell_size))
		elif map_level[x] == "2":
			display.blit(building, (x*cell_size,row*cell_size))

	return display

def display_spotlight(display,row):

	display.blit(spotlight,(searchlight_column*cell_size,row*cell_size))

	return display

def display_player(display,player_ypos,player_xpos):

	display.blit(player, (player_ypos*cell_size,player_xpos*cell_size))

	return display


"""

			if board[row][col] == "*":
				display.blit(player, (col * cell_size, row * cell_size))
			elif board[row][col] == "+":
				display.blit(stone, (col * cell_size, row * cell_size))
			elif board[row][col] == "O":
				display.blit(hole, (col * cell_size, row * cell_size))
			elif board[row][col] == "X":
				display.blit(skeleton, (col * cell_size, row * cell_size))
			elif board[row][col] == ":":
				display.blit(wall, (col * cell_size, row * cell_size))
"""


"""
<a href="https://www.flaticon.com/free-icons/tree" title="tree icons">Tree icons created by Freepik - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/resources" title="resources icons">Resources icons created by Smashicons - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/materials" title="materials icons">Materials icons created by Backwoods - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/illumination" title="illumination icons">Illumination icons created by surang - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/incognito" title="incognito icons">Incognito icons created by madness - Flaticon</a>
"""