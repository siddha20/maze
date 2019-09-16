if __name__ == "__main__":
	traps = 0
	size = 11
	grid = Grid(traps, size)
	grid.makeGrid()
	print(grid.map)
	player = Player()
	game = Game(grid, player)
	steps = 0
	screen=pygame.display.set_mode((900,900))
	screen.fill((255,255,255))
	pygame.display.update()
	for i in range(0,1):
		steps = 0
		game.re_init()
		while True:
			if game.done:
				print('game done with:', steps, 'steps')
				print(steps)
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
			pygame.display.update()
			state, reward, done, player_position = game.get_info()
			steps += 1
			print(player_position)
			print(reward)
			#time.sleep(3)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()




	

	


