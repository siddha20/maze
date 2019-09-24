from grid import Grid
from player import Player
from game import Game
from rendered_grid import RenderedGrid

import pygame
import numpy as np
import random
import time



if __name__ == "__main__":
	traps = 0
	size = 9
	grid = Grid(traps, size)
	grid.makeGrid()
	print(grid.map)

	player = Player()

	game = Game(grid, player)

	steps = 0
	screen=pygame.display.set_mode((900,900))
	screen.fill((255,255,255))

	render = RenderedGrid(screen)

	pygame.display.update()
	for i in range(0,1):
		steps = 0
		game.re_init()
		while True:
			if game.done:
				print('game done with:', steps, 'steps')
				print(steps)
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
			#game.render(screen)
			game.action_state(action)
			state, reward, done, player_position = game.get_info()
			render.makeRender(player_position)
			time.sleep(.05)
			#render.render_grid[3,3].change_color((133,234,218))
			pygame.display.update()
			steps += 1
			print(player_position)
			print(reward)
			#time.sleep(3)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()




	

	


