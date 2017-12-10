import pygame
import game_functions as gf

from settings import Settings
from snake import Snake_head
from growth_block import GrowthBlock
from message import Message

def run_game():
	# Initializes pygame and screen object, and instance of settings
	pygame.init()
	screen = pygame.display.set_mode((900, 650))
	game_settings = Settings()
	pygame.display.set_caption('Snake')
	
	# Initializes snake_head, growth_block, and creates list to store body_blocks in
	snake_head = Snake_head(screen, game_settings)
	growth_block = GrowthBlock(screen, game_settings)
	body_blocks = []
	

	
	while True:
		gf.check_events(snake_head, body_blocks, game_settings, growth_block)
		
		if game_settings.game_active:
			screen.fill(game_settings.screen_color)
			for i in range(len(body_blocks)):
				body_blocks[i].blitme()
		
			snake_head.update(growth_block, body_blocks)
			snake_head.blitme()
			growth_block.blitme()
			pygame.display.flip()
		else: 
			# When game is not active give Game over message, score, and msg to play again.
			message = Message(screen, snake_head)
			message.draw_msg()
			pygame.display.flip()	
run_game()
