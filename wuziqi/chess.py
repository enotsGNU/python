import pygame
from settings import Settings

class Chess():
	
	def __init__(self,screen):
		#flag 0 为黑棋
		self.flag = 0
		self.screen = screen
		self.set = Settings()
		#加载棋子图片
		self.white = pygame.image.load('baiqi1.png')
		self.black = pygame.image.load('heiqi1.png')

		self.white_rect = self.white.get_rect()
		self.black_rect = self.black.get_rect()
		#棋盘坐标列表
		self.chesslist = [[0 for i in range(self.set.columns_num + 1)]for i in range(self.set.row_num + 1)]

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

	def save_chess(self):
		if self.newx < 0 or self.newy < 0 or self.newy > self.set.row_num or self.newx > self.set.columns_num or self.chesslist[self.newy][self.newx] != 0:
			return 0
		if self.flag:
			#bai qi  -1
			self.chesslist[self.newy][self.newx] = -1
		else:		
			self.chesslist[self.newy][self.newx] = 1
		#print(self.chesslist)

	def coordinate(self):
		#棋子坐标由鼠标决定
		x,y = pygame.mouse.get_pos()
		#鼠标点击地方的棋子坐标
		self.newx = int((x + 25 - self.zerox)//50)
		self.newy = int((y + 25 - self.zeroy)//50)
		
		#print(self.newx,self.newy)
		if self.newx < 0 or self.newy < 0 or self.newy > self.set.row_num or self.newx > self.set.columns_num or self.chesslist[self.newy][self.newx] != 0:
			return 0
		self.white_rect.centerx = self.newx * 50 + self.zerox 
		self.white_rect.bottom = self.newy * 50 + self.zeroy + 25
		self.black_rect.centerx = self.newx * 50 + self.zerox
		self.black_rect.bottom = self.newy * 50 + self.zeroy + 25
		if self.flag:
			#flag 1 为白色
			self.screen.blit(self.white,self.white_rect)		
		else:
			self.screen.blit(self.black,self.black_rect)		
		self.flag = ~self.flag
		return 1
	
	def win(self):
		#白棋赢了-1 没人获胜　0
		winflag = 0
		i = self.chesslist[self.newy][self.newx]
		numi = 1
		nums = 1
		num1 = 1
		num2 = 1
		#下面的以后再改，反正也是复制的
		x = self.newx
		y = self.newy
		#竖直
		while(x >= 0 and y >= 0 and x <= self.set.columns_num and y <= self.set.row_num):
			a = self.chesslist[y][x]
			y = y -1
			if x < 0 or y < 0 or x > self.set.columns_num or y > self.set.row_num:
				break
			b = self.chesslist[y][x]
			if a == b:
				numi = numi + 1	
			else:
				break
		x = self.newx
		y = self.newy
		while(x >= 0 and y >= 0 and x <= self.set.columns_num and y <= self.set.row_num):
			a = self.chesslist[y][x]
			y = y + 1
			if x < 0 or y < 0 or x > self.set.columns_num or y > self.set.row_num:
				break
			b = self.chesslist[y][x]
			if a == b:
				numi = numi + 1	
			else:
				break
		x = self.newx
		y = self.newy
		#横向先左后右
		while(x >= 0 and y >= 0 and x <= self.set.columns_num and y <= self.set.row_num):
			a = self.chesslist[y][x]
			x = x -1
			if x < 0 or y < 0 or x > self.set.columns_num or y > self.set.row_num:
				break
			b = self.chesslist[y][x]
			if a == b:
				nums = nums + 1	
			else:
				break
		x = self.newx
		y = self.newy
		while(x >= 0 and y >= 0 and x <= self.set.columns_num and y <= self.set.row_num):
			a = self.chesslist[y][x]
			x = x + 1
			if x < 0 or y < 0 or x > self.set.columns_num or y > self.set.row_num:
				break
			b = self.chesslist[y][x]
			if a == b:
				nums = nums + 1	
			else:
				break


		x = self.newx
		y = self.newy
		#左斜
		while(x >= 0 and y >= 0 and x <= self.set.columns_num and y <= self.set.row_num):
			a = self.chesslist[y][x]
			x = x - 1
			y = y - 1
			if x < 0 or y < 0 or x > self.set.columns_num or y > self.set.row_num:
				break
			b = self.chesslist[y][x]
			if a == b:
				num1 = num1 + 1	
			else:
				break
		x = self.newx
		y = self.newy
		while(x >= 0 and y >= 0 and x <= self.set.columns_num and y <= self.set.row_num):
			a = self.chesslist[y][x]
			x = x + 1
			y = y + 1
			if x < 0 or y < 0 or x > self.set.columns_num or y > self.set.row_num:
				break
			b = self.chesslist[y][x]
			if a == b:
				num1 = num1 + 1	
			else:
				break


		x = self.newx
		y = self.newy
		#右斜
		while(x >= 0 and y >= 0 and x <= self.set.columns_num and y <= self.set.row_num):
			a = self.chesslist[y][x]
			x = x + 1
			y = y - 1
			if x < 0 or y < 0 or x > self.set.columns_num or y > self.set.row_num:
				break
			b = self.chesslist[y][x]
			if a == b:
				num2 = num2 + 1	
			else:
				break
		x = self.newx
		y = self.newy
		while(x >= 0 and y >= 0 and x <= self.set.columns_num and y <= self.set.row_num):
			a = self.chesslist[y][x]
			x = x - 1
			y = y + 1
			if x < 0 or y < 0 or x > self.set.columns_num or y > self.set.row_num:
				break
			b = self.chesslist[y][x]
			if a == b:
				num2 = num2 + 1	
			else:
				break


		if numi > 4 or nums > 4 or num1 > 4 or num2 > 4:
			winflag = i
			return winflag
		return 0
