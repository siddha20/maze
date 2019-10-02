from game.grid import Grid
from game.player import Player
from game.game import Game
from game.rendered_grid import RenderedGrid

import pygame
import numpy as np
import random
import time



if __name__ == "__main__":
	render = RenderedGrid()
	traps = 0
	size = 9
	grid = Grid(traps, size)
	grid.makeGrid()
	print(grid.map)

	game = Game(grid, Player(), RenderedGrid(), 30)

	

	pygame.display.update()
	for i in range(0,99):
		game.re_init()
		while True:
			if game.done:
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




	

	


