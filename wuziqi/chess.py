import pygame
from settings import Settings

class Chess():
	
	def __init__(self,screen):
		self.screen = screen
		self.set = Settings()
		#加载棋子图片
		self.white = pygame.image.load('baiqi1.png')
		self.black = pygame.image.load('heiqi1.png')

		self.white_rect = self.white.get_rect()
		self.black_rect = self.black.get_rect()

	def chessboard(self,screen):
		self.zerox = self.set.screen_width/2 - self.set.columns_num/2*self.set.row_width
		self.zeroy = self.set.screen_height/2 - self.set.row_num/2*self.set.row_width

		#画棋盘
		for i in range(0,self.set.row_num + 1):
			a = i * self.set.row_width
			pygame.draw.line(screen,self.set.qipan_color,(self.zerox,self.zeroy + a),(self.zerox + self.set.row_width * self.set.columns_num,self.zeroy + a),5)
		for i in range(0,self.set.columns_num + 1):
			a = i * self.set.row_width
			pygame.draw.line(screen,self.set.qipan_color,(self.zerox + a,self.zeroy),(self.zerox + a,self.zeroy + self.set.row_num * self.set.row_width),5)

	def blitme(self,flag):
		pass
	def num_chess(self):
		#棋盘坐标数字化，变成类似坐标1,1	1,2	....
		pass
	def coordinate(self,flag):
		#棋子坐标由鼠标决定
		x,y = pygame.mouse.get_pos()
		#鼠标点击地方的棋子坐标
		self.newx = int((x + 25 - self.zerox)//50)
		self.newy = int((y + 25 - self.zeroy)//50)
		
		print(self.newx,self.newy)
		if self.newx < 0 or self.newy < 0 or self.newy > self.set.row_num or self.newx > self.set.columns_num:
			return 0
		self.white_rect.centerx = self.newx * 50 + self.zerox 
		self.white_rect.bottom = self.newy * 50 + self.zeroy + 25
		self.black_rect.centerx = self.newx * 50 + self.zerox
		self.black_rect.bottom = self.newy * 50 + self.zeroy + 25
		if flag:
			#flag 1 为白色
			self.screen.blit(self.white,self.white_rect)		
		else:
			self.screen.blit(self.black,self.black_rect)		
