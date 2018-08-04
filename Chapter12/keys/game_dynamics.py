# Game functions
import sys
import pygame


def check_events(keys):
	"""Key events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown(event, keys)
		elif event.type == pygame.KEYUP:
			check_keydup(event, keys)


def check_keydown(event, keys):
	"""Respond keydown."""
	if event.key == pygame.K_RIGHT:
		keys.move_right = True
		print("You pressed " + hex(event.key) + " >> K_RIGHT")
	elif event.key == pygame.K_LEFT:
		keys.move_left = True
		print("You pressed " + hex(event.key) + " >> K_LEFT")
	elif event.key == pygame.K_UP:
		keys.move_top = True
		print("You pressed " + hex(event.key) + " >> K_UP")
	elif event.key == pygame.K_DOWN:
		keys.move_btm = True
		print("You pressed " + hex(event.key) + " >> K_DOWN")


def check_keydup(event, keys):
	"""Respond keydown."""
	if event.key == pygame.K_RIGHT:
		keys.move_right = False


def update_screen(gui_specs, screen):
	# update redrawing
	screen.fill(gui_specs.bg_color)

	# Most recent update
	pygame.display.flip()