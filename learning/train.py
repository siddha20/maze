from game.grid import Grid
from game.player import Player
from game.game import Game
from game.rendered_grid import RenderedGrid

from learning.q import Q

import pygame
import numpy as np
import random
import time	
import math

''' This will be the class where the game and the q class 
	come together one loop controlled the time (frames) '''

class Train:
	def __init__(self):
		self.frame_limit = None
		self.size =  None

		self.grid = None
		self.player = None
		self.grid_r = None
		self.game = None
		self.info = None
		
		self.q =  None
	def make_game(self, traps, size, square_size, frame_limit, rendered, epochs):
		self.size = size
		self.grid = Grid(traps, size)
		self.grid.makeGrid()
		self.player = Player()
		self.grid_r = RenderedGrid()
		self.game = Game(self.grid, self.player, self.grid_r,
		 square_size=square_size, frame_limit=frame_limit, rendered=rendered)
		self.frame_limit = self.game.frame_limit
		self.epochs = epochs

		self.q = Q((self.epochs*frame_limit))
		self.q.set_decay_variables(eps_max=1, eps_min=.1)
		self.q.create_table(size=self.size, num_actions=4) # 4 actions up down left right
		self.q.set_variables(learning_rate=.1, discount_rate=.97)
		print(self.q.decay)
		self.q.up_decay(.0002)

	def run_game(self, render_delay=0):
		steps = 0
		prev_q_state = 0
		for epoch in range(0, self.epochs):
			self.game.re_init()
			print(epoch)
			print(self.q.table)
			while True:

				if self.game.done or self.game.frame == self.frame_limit: #bug for some reason the game class doesnt stop it at frame limit all the time so i added it here
					break
				# get action from the Q class... for now it's random since class isn't finished
				action = self.q.get_action(prev_q_state)
				print(self.q.eps_val)
				self.game.action_state(action)
				state, reward, done, player_position, x, y = self.game.get_info()
				q_state = x * y
				#this is where the q value will be updated according to the next state
				
				self.q.update_table(prev_state=prev_q_state, state=q_state, action=action, reward=reward)
				prev_q_state = q_state
				self.q.eps_decay(steps)
				steps+=1




				time.sleep(render_delay) 
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						exit()

			




	

	
