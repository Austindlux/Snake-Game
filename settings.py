class Settings():
	"""Initializes game settings"""
	def __init__(self):
		# Screen settings
		self.screen_color = (60, 60, 60)
		
		# Snake settings
		self.snake_speed_factor = .69
		self.snake_color = (26, 210, 45)
				
		# Growth block settings
		self.growth_block_color = (255, 19, 0)

		self.game_active = True
