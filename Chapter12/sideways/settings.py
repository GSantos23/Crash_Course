# Settings 
class Settings():
	"""A class to store gui stuff."""
	def __init__(self):
		"""Initialize game settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (25,25,25)

		# Add speed factor
		self.rocket_speed = 2.5

		# Bullet settings
		self.bullet_speed = 1
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = 0,0,255
		self.bullet_allowed = 4
