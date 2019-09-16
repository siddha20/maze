class RenderedGrid: 
	def __init__(self, screen, model_player):
		self.screen = screen
		self.model = model_player
		self.size = int(np.shape(self.model)[0]
		self.render_grid = np.ndarray(shape=[self.size, self.size], dtype=object))
			for y in range(0,self.size):
				for x in range(0,self.size):
					render_grid[y,x] = Square()
	def makeRender(self, state): #needs to be run once to start the picture. 
		for y in range(0,self.size):
				for x in range(0,self.size):
					if state == 0:
						color = (255,255,255)
					if state == 1:
						color = (255,0,0)
					if state == 2:
						color = (0,255,0)
					render_grid[y,x].makeSquare(100, (100*x,y*100), color)

	def frame_change(self): #needs to be done after a action to update the frame