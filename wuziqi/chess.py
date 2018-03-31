import pygame

class Chess():
	
	def __init__(self,screen):
		self.screen = screen

		#加载棋子图片
		self.white = pygame.image.load('baiqi1.png')
		self.black = pygame.image.load('heiqi1.png')

		self.white_rect = self.white.get_rect()
		self.black_rect = self.black.get_rect()
		
	def blitme(self,flag):
		#棋子坐标由鼠标决定
		x,y = pygame.mouse.get_pos()
		self.white_rect.centerx = x 
		self.white_rect.bottom = y + 25
		self.black_rect.centerx = x 
		self.black_rect.bottom = y + 25
		if flag:
			#flag 1 为白色
			self.screen.blit(self.white,self.white_rect)		
		else:
			self.screen.blit(self.black,self.black_rect)		
	def num_chess():
		#棋盘坐标数字化，变成坐标1,1	1,2	....
		pass
	def coordinate():
		pass
	
