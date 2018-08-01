# Functions for the game
import sys
import pygame

def event_check():
	"""Respond to keypress and events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()


def screen_refresh(gui, screen, tux):
	"""Refresh screen."""
	screen.fill(gui.bg_color)
	tux.blitme()

	# Make the most recently draw screen visible
	pygame.display.flip()
