import pygame.font

class Message():
	def __init__(self, screen, snake_head):
		"""Initialize button attributes"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.screen_rect = screen.get_rect()
		self.score = snake_head.length
		
		# Background
		self.bg_height, self.bg_width = 140, 450
		self.bg_rect = pygame.Rect(0, 0, self.bg_width, self.bg_height)
		self.bg_rect.centerx = self.screen_rect.centerx
		self.bg_rect.centery = self.screen_rect.centery
		
		self.text_color = (0, 0, 0)
		self.font = pygame.font.SysFont(None, 48)
		
		self.prep_game_over()
		self.prep_score()
		self.prep_msg()
		
	def prep_game_over(self):
		"""Game over image above score"""
		self.game_over_image = self.font.render('Game Over', True, self.text_color, (110, 108, 108))
		self.game_over_rect = self.game_over_image.get_rect()
		self.game_over_rect.centery = self.screen_rect.centery - 35
		self.game_over_rect.centerx = self.screen_rect.centerx
		
	def prep_score(self):
		"""Score in the middle"""
		self.score_image = self.font.render('Score: ' + str(self.score), True, self.text_color, (110, 108, 108))
		self.score_rect = self.score_image.get_rect()
		self.score_rect.centery = self.screen_rect.centery 
		self.score_rect.centerx = self.screen_rect.centerx	
		
	def prep_msg(self):
		"""Msg below the score"""
		self.msg_image = self.font.render('Press Space To Play Again', True, self.text_color, (110, 108, 108))
		self.msg_rect = self.msg_image.get_rect()
		self.msg_rect.centery = self.screen_rect.centery + 35
		self.msg_rect.centerx = self.screen_rect.centerx	
		
	def draw_msg(self):
		"""Draws background, and each message/image."""
		self.screen.fill((110, 108, 108), self.bg_rect)
		self.screen.blit(self.game_over_image, self.game_over_rect)
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.msg_image, self.msg_rect)
