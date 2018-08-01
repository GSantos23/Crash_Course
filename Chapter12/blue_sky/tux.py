'''
Game Character: Find a bitmap image of a game character you like or
convert an image to a bitmap. Make a class that draws the character at the
center of the screen and match the background color of the image to the back-
ground color of the screen, or vice versa.
'''
# To manage tux -- the penguin
import pygame

class Tux():

	def __init__(self, screen):
		"""Initialize tux and set its starting position"""
		self.screen = screen

		# Load tux image and get its rectangle.
		self.image = pygame.image.load('images/tux.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start each new ship at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom


	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)