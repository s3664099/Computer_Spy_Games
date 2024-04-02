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
display_width = cell_size * columns
display_height = cell_size * rows
player = pygame.transform.scale(pygame.image.load("icons/spy.png"),(cell_size,cell_size))
rock = pygame.transform.scale(pygame.image.load("icons/rocks.png"),(cell_size,cell_size))
building = pygame.transform.scale(pygame.image.load("icons/building.png"),(cell_size,cell_size))
tree = pygame.transform.scale(pygame.image.load("icons/tree.png"),(cell_size,cell_size))
spotlight = pygame.transform.scale(pygame.image.load("icons/hole.png"),(cell_size,cell_size))
white = (255,255,255)

"""
<a href="https://www.flaticon.com/free-icons/tree" title="tree icons">Tree icons created by Freepik - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/resources" title="resources icons">Resources icons created by Smashicons - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/materials" title="materials icons">Materials icons created by Backwoods - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/illumination" title="illumination icons">Illumination icons created by surang - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/incognito" title="incognito icons">Incognito icons created by madness - Flaticon</a>
"""