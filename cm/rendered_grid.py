from square import Square
import numpy as np
class RenderedGrid: 
	def __init__(self, screen):
		self.screen = screen
		self.render_grid = None
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
					color = (255,255,255)
				if state == 1:
					color = (255,0,0)
				if state == 2:
					color = (0,255,0)
				if state == 99: #player
					color = (122,122,0)
				self.render_grid[y,x].makeSquare(100, (100*x,y*100), color)

	def frame_change(self): #needs to be done after a action to update the frame
		pass