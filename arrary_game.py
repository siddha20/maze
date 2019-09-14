import pygame
import sys
import random
import math
import numpy as np

np.random.seed(238)
#random.seed(299)


class Game: 
	def __init__(self, grid, player):
		self.grid = grid
		self.player = player
		self.position = np.zeros([2])
		self.position[0] = int(self.grid.size/2)
		self.position[1] = int(self.grid.size/2)
		self.player.update_position(self.position)
		self.state = self.grid.map[int(self.position[0]), int(self.position[1])]
		self.reward = None
		self.done = False
	def re_init(self):
		self.done = False
		self.position[0] = int(self.grid.size/2)
		self.position[1] = int(self.grid.size/2)
		self.reward = None
		self.state =  self.grid.map[int(self.position[0]), int(self.position[1])]
		return self.state
	def action_state(self, action):
		# bound check
		if int(self.position[1]) == (self.grid.size - 1) and action == 3:
			return 
		if int(self.position[1]) == 0 and action == 2:
			return 
		if int(self.position[0]) == 0 and action == 0:
			return 
		if int(self.position[0]) == (self.grid.size - 1) and action == 1:
			return 
		self.player.update_position(self.player.do_action(action))
		self.update_state()
		self.update_reward()
	def update_reward(self):
		if self.state == 1:
			self.reward = -100
			self.game_over()
		if self.state == 2:
			self.reward = 100
			self.game_over()
		if self.state == 0:
			self.reward = 10
	def update_state(self):
		self.state = self.grid.map[int(self.player.position[0]), int(self.player.position[1])]
	def game_over(self):
		self.done = True
	def get_info(self):
		return (self.state, self.reward, self.done, self.grid.model_player(self.position))

class Grid:
	def __init__(self, max_trap_per_row, size):
		self.map = np.zeros([size,size]) #size will be 8
		self.normal_square = 0
		self.bad_square = 1
		self.goal_square = 2
		self.size = size
		self.max_trap_per_row = max_trap_per_row

	def makeGrid(self):
		trap_x_count = 0
		goal_count = 0
		while not goal_count == 1:
			for y in range(0,self.map.shape[0]):
				trap_x_count = 0
				for x in range(0,self.map.shape[1]):
					rand = random.randint(0,100)
					if rand < 30 and self.map[y,x] == 0 and trap_x_count < self.max_trap_per_row:
						self.map[y,x] = self.bad_square
						trap_x_count += 1
					if rand > 90 and self.map[y,x] == 0 and goal_count == 0 and y > 3:
						self.map[y,x] = self.goal_square
						goal_count +=1
	def model_player(self, position):
		map_copy = np.copy(self.map)
		map_copy[int(position[0]), int(position[1])] = 99
		return map_copy

class Player:
	def __init__(self):
		self.position = None
		self.state = None
	def update_position(self, position):
		self.position = position
	def do_action(self, action): # up down left right 0 1 2 3
		if action == 0: 
			self.position[0] -= 1
		if action == 1:
			self.position[0] += 1
		if action == 2: 
			self.position[1] -= 1
		if action == 3:
			self.position[1] += 1
		return self.position	
	def get_position(self):
		return self.position


if __name__ == "__main__":
	traps = 0
	size = 11
	grid = Grid(traps, size)
	grid.makeGrid()
	print(grid.map)
	player = Player()
	game = Game(grid, player)
	steps = 0
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
			game.action_state(action)
			state, reward, done, player_position = game.get_info()
			steps += 1
			print(player_position)
			print(reward)




	

	


