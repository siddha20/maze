import random
import numpy as np
# integrate frames/steps into game
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