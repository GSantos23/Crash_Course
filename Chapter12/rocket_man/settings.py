# Settings 
class Settings():
	"""A class to store gui stuff."""
	def __init__(self):
		"""Initialize game settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (64,64,64)

		# Add speed factor
		self.rocket_speed = 2.5