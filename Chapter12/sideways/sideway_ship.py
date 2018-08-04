import pygame

class Sideway_Ship():
	def __init__(self, gui_specs, screen):
		"""Initializes the rocket on the middle of the screen."""
		self.screen = screen
		self.gui_specs = gui_specs

		# Load the image with its rectangle area
		self.image = pygame.image.load('Images/spaceship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start rock a the center of screen
		self.rect.centery = self.screen_rect.centery

		# Decimal value for center
		self.center_y = float(self.rect.centery)

		# Movement flag
		self.move_up = False
		self.move_down = False


	def update_position(self):
		"""Update rocket's postion."""
		# Update rocket center value
		if self.move_up and self.rect.top > 0:
			self.center_y -= self.gui_specs.rocket_speed
		if self.move_down and self.rect.bottom < self.screen_rect.bottom:
			self.center_y += self.gui_specs.rocket_speed

		# update self.center
		self.rect.centery = self.center_y


	def draw_rocket(self):
		"""Draw the rocket."""
		self.screen.blit(self.image, self.rect)