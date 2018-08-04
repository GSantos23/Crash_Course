# Basic structure of a game using pygame
#import sys -> We don't need this anymore thanks to game_functions.py
import pygame
import game_functions as gf

from pygame.sprite import Group
from settings import Settings	
from ship import Ship			


def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	(ai_settings.screen_width, ai_settings.screen_height))

	# set_mode((width, height))	!!!
	pygame.display.set_caption("Alien Invasion")

	# Make a ship.
	ship = Ship(ai_settings, screen)
	# Make a group to store bullets in.
	bullets = Group()

	# Start the main loop for the game
	while True:
		# Watch for keyboard and mouse events.
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		# Bullets
		gf.update_bullets(bullets)
		# Redraw screen and images
		gf.update_screen(ai_settings, screen, ship, bullets)


run_game()