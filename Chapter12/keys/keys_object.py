import pygame

class Keys_Object():
	def __init__(self, gui_specs, screen):
		"""Screen specs."""
		self.screen = screen
		self.gui_specs = gui_specs

		# Movement flag
		self.move_right = False
		self.move_left = False
		self.move_top = False
		self.move_btm = False

		