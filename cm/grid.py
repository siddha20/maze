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