# Game functions with refactoring code
import sys
import pygame

from bullet import Bullet

def check_events(gui_specs, screen, rocket, bullets):
	"""Keyevents."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown(event, gui_specs, screen, rocket, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup(event, rocket)


def check_keydown(event, gui_specs, screen, rocket, bullets):
	if event.key == pygame.K_UP:
		rocket.move_up = True
	elif event.key == pygame.K_DOWN:
		rocket.move_down = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(gui_specs, screen, rocket, bullets)


def check_keyup(event, rocket):
	if event.key == pygame.K_UP:
		rocket.move_up = False
	elif event.key == pygame.K_DOWN:
		rocket.move_down = False


def update_screen(gui_specs, screen, rocket, bullets):
	"""Update images on the screen and flip to new screen."""
	# Redraw screen
	screen.fill(gui_specs.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	rocket.draw_rocket()

	# Most recent screen visible
	pygame.display.flip()


def fire_bullet(gui_specs, screen, rocket, bullets):
	"""Fire a bullet if limit not reached yet."""
	if len(bullets) < gui_specs.bullet_allowed:
		new_bullet = Bullet(gui_specs, screen, rocket)
		bullets.add(new_bullet)


def update_bullets(bullets):
	"""Update position of bullets and get rid of old bullets."""
	# Update bullet positions
	bullets.update()

	# Get rid of old bullets
	for bullet in bullets.copy():
		if bullet.rect.right >= 1200:
			bullets.remove(bullet)