import pygame
from random import randint

class GrowthBlock():
	def __init__(self, screen, game_settings):
		"""Creates a new growth block that is randomly placed on screen"""
		self.screen = screen
		self.color = game_settings.growth_block_color
		
		# Sets rect at origin and size 25 x 25
		self.rect = pygame.Rect(0, 0, 24, 24)
		
		# Uses randint to use as random rect position
		x = randint(0, 35)
		y = randint(1, 26)
		self.rect.x = (25 * x) + 1
		self.rect.bottom = 25 * y
		
	def blitme(self):
		pygame.draw.rect(self.screen, self.color, self.rect)		

	def new_block(self, body_blocks, snake_head):
		"""Sets block in new position"""
		x = randint(0, 35)
		y = randint(1, 26)
		self.rect.x = (25 * x) + 1
		self.rect.bottom = 25 * y
		
		# If new block is on snake, get new block
		if self.rect.x == snake_head.rect.x and self.rect.bottom == snake_head.rect.bottom:
			self.new_block(body_blocks, snake_head)
		
		# If new block is on any body block, get new block
		if body_blocks:
			for i in range(len(body_blocks)):
				if self.rect.x == body_blocks[i].rect.x and self.rect.bottom == body_blocks[i].rect.bottom:
					self.new_block(body_blocks, snake_head)
