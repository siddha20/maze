import pygame
import sys
import random
import math
import numpy as np

np.random.seed(238)
random.seed(299)


class Grid:
	def __init__(self, trap_num, size):
		self.map = np.zeros([size,size]) #size will be 8
		self.normal_square = 0
		self.bad_square = 1
		self.goal_square = 2
		self.trap_num = trap_num
		self.size = size

	def makeGrid(self):
		trap_x_count = 0
		goal_count = 0
		while not goal_count == 1:
			for y in range(0,self.map.shape[0]):
				trap_x_count = 0
				for x in range(0,self.map.shape[1]):
					rand = random.randint(0,100)
					if rand < 30 and self.map[y,x] == 0 and trap_x_count < 2:
						self.map[y,x] = self.bad_square
						trap_x_count += 1
					if rand > 90 and self.map[y,x] == 0 and goal_count == 0 and y > 3:
						self.map[y,x] = self.goal_square
						goal_count +=1

class Player:
	def __init__(self, grid):
		self.grid = grid
		self.position = np.zeros([2])
		self.state = None
		self.latest_reward = None
		self.position[0] = int(self.grid.size/2)
		self.position[1] = int(self.grid.size/2)
		self.done = False
		self.update_state()

	def do_action(self, action): # up down left right 0 1 2 3
		if action == 0: 
			self.position[0] -= 1
		if action == 1:
			self.position[0] += 1
		if action == 2: 
			self.position[1] -= 1
		if action == 3:
			self.position[1] += 1	
		self.latest_reward = self.update_state()

	def update_state(self):
		self.state = grid.map[int(self.position[0]), int(self.position[1])]
		reward = 0
		if self.state == 1:
 			reward = -100
 			self.done = True
 			self.reset()
		if self.state == 2:
			reward = 100
			self.done = True
			self.reset()
		if self.state == 0:
			reward = 10
		return reward

	def reset(self):
		self.position[0] = int(self.grid.size/2)
		self.position[1] = int(self.grid.size/2)
		self.done = False 

	def get_info(self):
		return(self.state, self.latest_reward, self.position, self.done)		

if __name__ == "__main__":
	grid = Grid(18,9)
	grid.makeGrid()
	print(grid.map)
	player = Player(grid)
	player.reset()
	count = 0
	while True:
		print(count)
		player.do_action(3)
		state, reward, position, done = player.get_info()
		print(state, reward, position, done)
		if player.done:
			break
		count += 1

	


