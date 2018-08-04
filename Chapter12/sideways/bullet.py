# Bullet Class
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage bullets fired from the ship."""
	def __init__(self, gui_specs, screen, rocket):
		"""Create a bullet object at ship's position."""
		super(Bullet, self).__init__()
		self.screen = screen

		# Create a bullet rectangle
		self.rect = pygame.Rect(0,0, gui_specs.bullet_width, 
			gui_specs.bullet_height)
		self.rect.centery = rocket.rect.centery
		self.rect.right = rocket.rect.right

		# Store the bullet's position as a decimal value
		self.x = float(self.rect.x)

		self.color = gui_specs.bullet_color
		self.bllt_speed = gui_specs.bullet_speed


	def update(self):
		"""Move the bullet right the screen."""
		self.x += self.bllt_speed
		self.rect.x = self.x


	def draw_bullet(self):
		"""Draw the bullet to the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)