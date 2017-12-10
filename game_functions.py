import sys
import pygame

from growth_block import GrowthBlock
from body_block import BodyBlock
	
def clear_movement_flags(snake_head):
	"""Resets movement flags of snake head to false"""
	snake_head.moving_right = False
	snake_head.moving_left = False
	snake_head.moving_up = False
	snake_head.moving_down = False

def check_events(snake_head, body_blocks, game_settings, growth_block):
	"""respond to keypresses"""
	
	# True means it is allowed to go in that direction
	sideways = True
	vertical = True
	# Cant go to the left if you have a body block to the left...
	if body_blocks:
		if snake_head.rect.bottom == body_blocks[0].rect.bottom:
			sideways = False
		if snake_head.rect.x == body_blocks[0].rect.x:
			vertical = False
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				sys.exit()
			if event.key == pygame.K_RIGHT and sideways:
				clear_movement_flags(snake_head)
				snake_head.moving_right = True
			if event.key == pygame.K_LEFT and sideways:
				clear_movement_flags(snake_head)
				snake_head.moving_left = True
			if event.key == pygame.K_UP and vertical:
				clear_movement_flags(snake_head)
				snake_head.moving_up = True
			if event.key == pygame.K_DOWN and vertical:
				clear_movement_flags(snake_head)
				snake_head.moving_down = True
			if not game_settings.game_active and event.key == pygame.K_SPACE:
				reset_game(snake_head, body_blocks, game_settings, growth_block)
				
def reset_game(snake_head, body_blocks, game_settings, growth_block):
	# Delete all body blocks
	body_blocks.clear()
	
	# Reset snake 
	clear_movement_flags(snake_head)
	snake_head.length = 0
	snake_head.color = game_settings.snake_color
	snake_head.rect.x = 1
	snake_head.rect.y = 1
	snake_head.center = float(snake_head.rect.centerx)
	snake_head.bottom = float(snake_head.rect.bottom)
	growth_block.new_block(body_blocks, snake_head)			
	
	# Game active
	game_settings.game_active = True	


def snake_hit_block(growth_block, screen, game_settings, snake_head, body_blocks):
	# Sets new position for growth block
	growth_block.new_block(body_blocks, snake_head)
	snake_head.length += 3
	
	# Adds 3 new body blocks 
	for _ in range(3):
		index_in_list = len(body_blocks)
		new_body_block = BodyBlock(screen, game_settings, index_in_list)
		body_blocks.append(new_body_block)
		new_body_block.set_start_position(snake_head, body_blocks)	
		
def update_body(snake_head, body_blocks):
	if body_blocks:
		body_blocks[-1].update(snake_head, body_blocks)
	
def game_done(game_settings, snake_head, body_blocks):
	"""Stops the game"""
	game_settings.game_active = False
	snake_head.color = (255, 255, 255)
	
	# draw body to screen before the game stops
	for i in range(len(body_blocks)):
		body_blocks[i].blitme()
	pygame.display.flip()
	
def check_snake_hit_body(snake_head, body_blocks, game_settings):
	"""Checks if the snake has hit any body blocks"""
	if body_blocks:
		
		# Counting number of body_blocks the snake head it hitting
		count = 0
		for i in range(len(body_blocks)):
			if snake_head.rect.x == body_blocks[i].rect.x and snake_head.rect.bottom == body_blocks[i].rect.bottom:
				count += 1
			
		# The snake hits 3 body blocks when it eats the first growth block and therefore not a game over
		if count == 3 or count == 0:
			pass
		else:
			game_done(game_settings, snake_head, body_blocks)
			
def check_snake_hit_edge(game_settings, snake_head, body_blocks):
	"""Checks if the snake has hit the edge of the screen"""
	if snake_head.rect.x >= 900 or snake_head.rect.x <= 0 or snake_head.rect.y >= 650 or snake_head.rect.y <= 0:
		game_done(game_settings, snake_head, body_blocks)
