# Basic structure of a game using pygame
#import sys -> We don't need this anymore thanks to game_functions.py
import pygame
import game_functions as gf

from pygame.sprite import Group
from settings import Settings	
from ship import Ship	
from game_stats import GameStats		


def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	(ai_settings.screen_width, ai_settings.screen_height))

	# set_mode((width, height))	!!!
	pygame.display.set_caption("Alien Invasion")

	# Make a ship, a group of bullets, and a group of aliens. 
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()

	# Make an instance to store game statistics
	stats = GameStats(ai_settings)

	# Create fleet of aliens
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# Start the main loop for the game
	while True:
		# Watch for keyboard and mouse events.
		gf.check_events(ai_settings, screen, ship, bullets)

		if stats.game_active:
			ship.update()
			# Bullets
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			# Aliens
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
		# Redraw screen and images
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()