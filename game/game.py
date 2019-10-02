import random
import numpy as np
# integrate frames/steps into game
class Game: 
	def __init__(self, grid, player, render, square_size=100, frame_limit=75, rendered=True):
		self.grid = grid
		self.player = player
		self.position = np.zeros([2])
		self.position[0] = int(self.grid.size/2)
		self.position[1] = int(self.grid.size/2)
		self.player.update_position(self.position)
		self.state = self.grid.map[int(self.position[0]), int(self.position[1])]
		self.reward = None
		self.done = False
		self.render = render
		self.rendered = rendered
		self.frame = 0
		self.frame_limit = frame_limit
		self.render.set_variables((int(self.grid.size)), square_size)
		self.color = [0,200,0]
	def re_init(self): #needs to be called after game over 
		self.done = False
		self.frame = 0
		self.position[0] = int(self.grid.size/2)
		self.position[1] = int(self.grid.size/2)
		self.reward = None
		self.state =  self.grid.map[int(self.position[0]), int(self.position[1])]
		return self.state
	def action_state(self, action):
		# bound check
		self.frame = self.frame + 1
		if int(self.position[1]) == (self.grid.size - 1) and action == 3:
			return 
		if int(self.position[1]) == 0 and action == 2:
			return 
		if int(self.position[0]) == 0 and action == 0:
			return 
		if int(self.position[0]) == (self.grid.size - 1) and action == 1:
			return 
		old_position = self.player.position
		self.player.update_position(self.player.do_action(action))
		self.update_state()
		self.update_reward()
		if(self.rendered):
			self.frame_update(self.grid.model_player(self.position))
			if(self.color[0] >= 255 or self.color[1] < 255): 
				self.color[1] = self.color[1]+1
			else: 
				self.color[0] = self.color[0] + 1
			if(self.color[1] >= 255):
				self.color[2] = self.color[2]+1
			if(self.color[2] >= 100):
				self.color = [0,200,0]
		

			self.render.update_frame(self.position, self.color)
		print("frame: ", self.frame, "color: ", self.color )
	def update_reward(self):
		if self.frame == self.frame_limit:
			self.game_over() 
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
	def frame_update(self, model):
		if(self.frame == 1):
			#do the frame init for render	
			self.render.makeRender(model)	
