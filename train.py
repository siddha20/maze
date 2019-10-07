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
	come together one loop controlled the time (frames)'''

class Train:
	def __init__(self):
		self.frame_limit = None
		self.size =  None

		self.grid = None
		self.player = None
		self.grid_r = None
		self.game = None
		self.info = None
		
		self.frame = None
	def make_game(self, traps, size, square_size, frame_limit, rendered):
		self.size = size
		self.grid = Grid(traps, size)
		self.grid.makeGrid()
		self.player = Player()
		self.grid_r = RenderedGrid()
		self.game = Game(self.grid, self.player, self.grid_r,
		 square_size=square_size, frame_limit=frame_limit, rendered=rendered)
		self.frame_limit = self.game.frame_limit

	def run_game(self, epochs, render_delay=0):
			for i in range(0, epochs):
				self.game.re_init()
				while True:
					self.frame = self.game.frame
					if self.game.done:
						break
					# get action from the Q class... for now it's random since class isn't finished

					action = random.randint(0,3)
					self.game.action_state(action)
					state, reward, done, player_position = self.game.get_info()
					self.info = (state, reward, done,  player_position)
					#this is where the q value will be updated according to the next state

					prev_state = state

					
					time.sleep(render_delay) 
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
							exit()

			




	

	
