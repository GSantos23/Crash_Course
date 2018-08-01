# Blue Sky: Make a Pygame window with a blue background.
#import sys
import pygame
import dynamics as dyn

from settings import Settings
from tux import Tux

def start_game():
	# Initiliaze a blue screen
	pygame.init()
	gui = Settings()	# Add features from settings.py
	screen = pygame.display.set_mode((gui.screen_width,	 gui.screen_height))

	tux = Tux(screen)

	# Set caption 
	pygame.display.set_caption("Blue Sky")

	while True:
		# Events check
		dyn.event_check()
		# Blue screen
		dyn.screen_refresh(gui, screen, tux)


start_game()