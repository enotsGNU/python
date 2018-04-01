#五子棋
import pygame
import sys
from pygame.locals import *
from settings import Settings
from chess import Chess
def run_game():
	global flag
	
	#创建屏幕对象
	pygame.init()
	qiset = Settings()
	screen = pygame.display.set_mode((qiset.screen_width,qiset.screen_height))
	pygame.display.set_caption("五子棋")
	chess = Chess(screen) 
	a = 0
		
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
							a=chess.coordinate()
							if a:
								chess.save_chess()
								b = chess.win()
								if b == 1:
									print('白棋赢了')
								elif b == -1:
									print('黑棋赢了')
						elif i == 1:
							#mouse wheel
							pass
						elif i == 2:
							pass
							#right button
		#让最近绘制的屏幕可见
		pygame.display.flip()
run_game()
