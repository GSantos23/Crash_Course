# Exercise 12.4
import pygame
import game_dynamics as dyn

from settings import Settings
from keys_object import Keys_Object

def game_init():
	# Initialize elements
	pygame.init()
	gui_specs = Settings()
	screen = pygame.display.set_mode((gui_specs.screen_width, 
		gui_specs.screen_height))

	# Set caption
	pygame.display.set_caption("Keys...")

	# Make KEys object
	keys = Keys_Object(gui_specs, screen)

	# Event Loop
	while True:
		# Refresh key events
		dyn.check_events(keys)
		# Refresh screen
		dyn.update_screen(gui_specs,screen)


game_init()