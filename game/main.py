from grid import Grid
from player import Player
from game import Game
from rendered_grid import RenderedGrid

import pygame
import numpy as np
import random
import time



if __name__ == "__main__":
	render = RenderedGrid()
	traps = 0
	size = 129
	grid = Grid(traps, size)
	grid.makeGrid()
	print(grid.map)

	game = Game(grid, Player(), RenderedGrid(), 9)

	

	pygame.display.update()
	for i in range(0,1):
		game.re_init()
		while True:
			if game.done:
				time.sleep(10)
				break
			action = random.randint(0,3)
			if action == 0:
				print('up')
			if action == 1:
				print('down')
			if action == 2:
				print('left')
			if action == 3:
				print('right')
			game.action_state(action)
			state, reward, done, player_position = game.get_info()
			time.sleep(.01)
			pygame.display.update()
			print(player_position)
			print(reward)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()




	

	


