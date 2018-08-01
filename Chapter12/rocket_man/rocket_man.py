# Rocket game
import pygame
import game_dynamics as dyn

from settings import Settings
from rocket_ship import Rocket_Ship

def launch():
	# Initializes elemets for rocket game.
	pygame.init()
	gui_specs = Settings()
	screen = pygame.display.set_mode(
		(gui_specs.screen_width, gui_specs.screen_height))

	# set caption
	pygame.display.set_caption("Rocket man...")

	# Make Rocket
	rocket = Rocket_Ship(gui_specs, screen)

	# Start event loop
	while True:
		# Refresh position and key events
		dyn.check_events(rocket)
		rocket.update_position()
		# Refresh screen
		dyn.update_screen(gui_specs, screen, rocket)


launch()