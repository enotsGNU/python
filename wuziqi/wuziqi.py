#五子棋
import pygame
import sys
from pygame.locals import *
from settings import Settings
from chess import Chess
flag = 0
'''
#传入屏幕对象
def init_chessboard(screen):
	qiset = Settings()
	zerox = qiset.screen_width/2 - qiset.columns_num/2*qiset.row_width
	zeroy = qiset.screen_height/2 - qiset.row_num/2*qiset.row_width
	
	#画棋盘
	for i in range(0,qiset.row_num + 1):
		a = i * qiset.row_width
		pygame.draw.line(screen,qiset.qipan_color,(zerox,zeroy + a),(zerox + qiset.row_width*qiset.columns_num,zeroy + a),5)
	for i in range(0,qiset.columns_num + 1):
		a = i * qiset.row_width
		pygame.draw.line(screen,qiset.qipan_color,(zerox + a,zeroy),(zerox + a,zeroy + qiset.row_num * qiset.row_width),5)
'''
def run_game():
	global flag
	
	#创建屏幕对象
	pygame.init()
	qiset = Settings()
	screen = pygame.display.set_mode((qiset.screen_width,qiset.screen_height))
	pygame.display.set_caption("五子棋")
	chess = Chess(screen) 
	
		
	#bg_color
	screen.fill(qiset.bg_color)
	#绘制棋盘
	chess.chessboard(screen)	

	#main()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == MOUSEBUTTONDOWN:
				pressed_array = pygame.mouse.get_pressed()
				for i in range(len(pressed_array)):
					if pressed_array[i]:
						if i == 0:
							#left button
							#chess.blitme(flag)
							chess.coordinate(flag)
							flag = ~flag
						elif i == 1:
							#mouse wheel
							pass
						elif i == 2:
							pass
							#right button
							#chess.coordinate(flag)

		#让最近绘制的屏幕可见
		pygame.display.flip()
run_game()
