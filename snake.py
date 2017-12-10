import pygame
import game_functions as gf

class Snake_head():
	def __init__(self, screen, game_settings):
		self.screen = screen
		self.game_settings = game_settings
		self.color = game_settings.snake_color
		self.length = 0 
		
		# Sets snakes rect at (0, 0) and size 25 x 25
		self.rect = pygame.Rect(1, 1, 24, 24)
		
		# Decimal for snake_heads rect
		self.center = float(self.rect.centerx)
		self.bottom = float(self.rect.bottom)
 
		# Movement flags
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def blitme(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
		
		
	def update(self, growth_block, body_blocks):
		if self.moving_right:
			self.center += self.game_settings.snake_speed_factor
		if self.moving_left:
			self.center -= self.game_settings.snake_speed_factor			
		if self.moving_up:
			self.bottom -= self.game_settings.snake_speed_factor
		if self.moving_down:
			self.bottom += self.game_settings.snake_speed_factor

		# Updates rect once it moves over 25
		if self.center >= (self.rect.centerx + 25):
			gf.update_body(self, body_blocks)
			self.rect.x += 25
			check_snake_hit_block(self, growth_block, body_blocks)
			gf.check_snake_hit_body(self, body_blocks, self.game_settings)
			gf.check_snake_hit_edge(self.game_settings, self, body_blocks)		
		if self.center <= (self.rect.centerx - 25):
			gf.update_body(self, body_blocks)
			self.rect.x -= 25
			check_snake_hit_block(self, growth_block, body_blocks)	
			gf.check_snake_hit_body(self, body_blocks, self.game_settings)	
			gf.check_snake_hit_edge(self.game_settings, self, body_blocks)
		if self.bottom >= (self.rect.bottom + 25):
			gf.update_body(self, body_blocks)
			self.rect.bottom += 25
			check_snake_hit_block(self, growth_block, body_blocks)	
			gf.check_snake_hit_body(self, body_blocks, self.game_settings)	
			gf.check_snake_hit_edge(self.game_settings, self, body_blocks)
		if self.bottom <= (self.rect.bottom - 25):
			gf.update_body(self, body_blocks)
			self.rect.bottom -=25
			check_snake_hit_block(self, growth_block, body_blocks)
			gf.check_snake_hit_body(self, body_blocks, self.game_settings)
			gf.check_snake_hit_edge(self.game_settings, self, body_blocks)
			

def check_snake_hit_block(snake_head, growth_block, body_blocks):
	"""Check if snake hit growth block, If it has it sets new position for growth_block and adds 3 body blocks"""
	if growth_block.rect.x == snake_head.rect.x and growth_block.rect.bottom == snake_head.rect.bottom:
		gf.snake_hit_block(growth_block, snake_head.screen, snake_head.game_settings, snake_head, body_blocks)
	

