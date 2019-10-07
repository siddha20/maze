from game.square import Square
import numpy as np
import pygame
class RenderedGrid: 
	def __init__(self): #screen size needs a number before running makeRender
		self.render_grid = None
		self.screen_size = None
		self.square_size = None
	def makeRender(self, model_player): #needs to be run once to start the picture. 
		self.size = int(np.shape(model_player)[0])
		self.render_grid = np.ndarray(shape=[self.size, self.size], dtype=object)
		for y in range(0,self.size):
			for x in range(0,self.size):
				self.render_grid[y,x] = Square(self.screen)
		for y in range(0,self.size):
			for x in range(0,self.size):
				state = model_player[y,x]
				if state == 0:
					color = (0,0,0)
				if state == 1:
					color = (255,0,0)
				if state == 2:
					color = (255,255,0)
				if state == 99: #player
					color = (122,122,0)
				self.render_grid[y,x].makeSquare(self.square_size, (self.square_size*x,y*self.square_size), color)
		pygame.display.update()
	def update_frame(self, cur_pos, color_list):
		color = (color_list[2], color_list[0], color_list[1])
		self.render_grid[int(cur_pos[0]),int(cur_pos[1])].change_color(color)
		pygame.display.update()
	def set_variables(self, trap_num, square_size): #needs to be done after a action to update the frame
		self.square_size = square_size
		self.screen_size = trap_num * self.square_size
		self.screen=pygame.display.set_mode((self.screen_size,self.screen_size))
		self.screen.fill((255,255,255))
		pygame.display.update()