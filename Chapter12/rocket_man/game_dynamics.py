# Game functions with refactoring code
import sys
import pygame

def check_events(rocket):
	"""Keyevents."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown(event, rocket)
		elif event.type == pygame.KEYUP:
			check_keyup(event, rocket)

	# Code for movement

def check_keydown(event, rocket):
	"""Respond to keypress."""
	if event.key == pygame.K_RIGHT:
		rocket.move_right = True
	elif event.key == pygame.K_LEFT:
		rocket.move_left = True
	elif event.key == pygame.K_UP:
		rocket.move_up = True
	elif event.key == pygame.K_DOWN:
		rocket.move_down = True


def check_keyup(event, rocket):
	if event.key == pygame.K_RIGHT:
		rocket.move_right = False
	elif event.key == pygame.K_LEFT:
		rocket.move_left = False
	elif event.key == pygame.K_UP:
		rocket.move_up = False
	elif event.key == pygame.K_DOWN:
		rocket.move_down = False


def update_screen(gui_specs, screen, rocket):
	"""Update images on the screen and flip to new screen."""
	# Redraw screen
	screen.fill(gui_specs.bg_color)
	rocket.draw_rocket()

	# Most recent screen visible
	pygame.display.flip()