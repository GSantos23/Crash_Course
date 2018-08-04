# Rocket game
import pygame
import game_dynamics as dyn

from pygame.sprite import  Group
from settings import Settings
from sideway_ship import Sideway_Ship

def launch():
	# Initializes elemets for rocket game.
	pygame.init()
	gui_specs = Settings()
	screen = pygame.display.set_mode(
		(gui_specs.screen_width, gui_specs.screen_height))

	# set caption
	pygame.display.set_caption("Sideway ...")

	# Make Rocket
	rocket = Sideway_Ship(gui_specs, screen)

	# Store bullets
	bullets = Group()

	# Start event loop
	while True:
		# Refresh position and key events
		dyn.check_events(gui_specs, screen, rocket, bullets)
		rocket.update_position()
		# Bullets
		dyn.update_bullets(bullets)
		# Refresh screen
		dyn.update_screen(gui_specs, screen, rocket, bullets)


launch()