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
