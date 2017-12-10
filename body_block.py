import pygame

class BodyBlock():
	def __init__(self, screen, game_settings, index_in_list):
		self.index_in_list = index_in_list
		self.screen = screen
		self.color = game_settings.snake_color
		self.rect = pygame.Rect(0, 0, 24, 24)
		
	def set_start_position(self, snake_head, body_blocks):
		"""Sets start position at same spot as block before it"""
		if self.index_in_list == 0:
			self.rect.centerx = snake_head.rect.centerx 
			self.rect.bottom = snake_head.rect.bottom 

		else:
			self.rect.centerx = body_blocks[self.index_in_list - 1].rect.centerx 
			self.rect.bottom = body_blocks[self.index_in_list - 1].rect.bottom 
											
				
	def update(self, snake_head, body_blocks):
		"""Sets the position of each block at the position of the block before it. Starting from last block"""
		if self.index_in_list == 0:
			self.rect.x = snake_head.rect.x
			self.rect.bottom = snake_head.rect.bottom
		
		else: 
			self.rect.x = body_blocks[self.index_in_list - 1].rect.x
			self.rect.bottom = body_blocks[self.index_in_list - 1].rect.bottom
			body_blocks[self.index_in_list - 1].update(snake_head, body_blocks)
			
			
	def blitme(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
