class GameStats():
	"""Track statidtics for Alien Invasion."""

	def __init__(self, ai_settings):
		"""Initialiaze statistics."""
		self.ai_settings = ai_settings
		self.reset_stats()
		# Start Alien Invsion in active state.  
		self.game_active = True


	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.ai_settings.ship_limit
